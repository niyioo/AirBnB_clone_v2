#!/usr/bin/python3
"""
This Fabric script deploys an archive to web servers.
"""

from fabric.api import env, put, run
import os.path

# Specify the SSH user and web server IP addresses
env.hosts = ['54.236.30.173', '100.26.56.25']


def do_deploy(archive_path):
    """
    Distribute an archive to web servers and update the current symlink.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    # Check if the archive file exists
    if os.path.isfile(archive_path) is False:
        return False

    # Extract the filename and name (without extension) from the archive path
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    # Upload the archive to /tmp/ on the web server
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False

    # Remove the existing release folder
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False

    # Create the release folder
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False

    # Uncompress the archive into the release folder
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed is True:
        return False

    # Remove the uploaded archive
    if run("rm /tmp/{}".format(file)).failed is True:
        return False

    # Move the contents of the release folder
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False

    # Remove the redundant web_static subfolder
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed is True:
        return False

    # Remove the existing current symlink
    if run("rm -rf /data/web_static/current").failed is True:
        return False

    # Create a new symlink to the latest release
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
        return False

    # Return True if all operations were successful
    return True
