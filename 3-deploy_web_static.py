#!/usr/bin/python3
"""
This Fabric script creates and distributes an archive to web servers.
"""

import os
import re
from fabric.api import *
from datetime import datetime

env.user = "ubuntu"
env.hosts = ["54.236.30.173", "100.26.56.25"]
env.key_filename = "~/id_rsa"


def do_pack():
    """
    Generate a .tgz archive of web_static and store it in the versions folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    target = local("mkdir -p versions")
    name = str(datetime.now()).replace(" ", '')
    opt = re.sub(r'[^\w\s]', '', name)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(opt))
    if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(opt))
    else:
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to web servers and update the current symlink.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if not os.path.isfile(archive_path):
        return False

    # Extract the filename and name (without extension) from the archive path
    file = os.path.basename(archive_path)
    name = os.path.splitext(file)[0]

    # Upload the archive to /tmp/ on the web server
    put(archive_path, "/tmp/{}".format(file))

    # Remove the existing release folder
    run("rm -rf /data/web_static/releases/{}/".format(name))

    # Create the release folder
    run("mkdir -p /data/web_static/releases/{}/".format(name))

    # Uncompress the archive into the release folder
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name))

    # Remove the uploaded archive
    run("rm /tmp/{}".format(file))

    # Move the contents of the release folder
    run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(name, name))

    # Remove the redundant web_static subfolder
    run("rm -rf /data/web_static/releases/{}/web_static".format(name))

    # Remove the existing current symlink
    run("rm -rf /data/web_static/current")

    # Create a new symlink to the latest release
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(name))

    print("New version deployed!")
    return True


def deploy():
    """
    Deploy the web_static archive to web servers.

    Returns:
        True if the deployment is successful, otherwise False.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
