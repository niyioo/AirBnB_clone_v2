#!/usr/bin/python3
"""
This Fabric script deploys an archive to web servers.
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os.path

# Specify the SSH user and web server IP addresses
env.user = 'ubuntu'
env.hosts = ['54.236.30.173', '100.26.56.25']


def do_pack():
    """
    Generate a .tgz archive of web_static and store it in the versions folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Create the 'versions' directory if it doesn't exist
        local("mkdir -p versions")

        # Compress the 'web_static' directory into a .tgz archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Display the packed files
        local("tar tvf versions/{}".format(archive_name))

        return "versions/{}".format(archive_name)
    except Exception:
        return None

if __name__ == "__main__":
    result = do_pack()
    if result:
        print("Archive created:", result)
    else:
        print("Archive creation failed.")


def do_deploy(archive_path):
    """
    Distribute an archive to web servers and update the current symlink.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """
    Deploy the web_static content to the web servers.
    """
    archive_path = do_pack()

    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
