#!/usr/bin/python3
"""
This Fabric script deploys an archive to web servers.
"""
from fabric.api import env, put, run, sudo
import os

# Specify the SSH user and web server IP addresses
env.user = 'ubuntu'
env.hosts = ['100.26.56.25', '54.89.25.134']


def do_deploy(archive_path):
    """
    Distribute an archive to web servers and update the current symlink.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False

    # Extract archive filename without extension
    archive_filename = os.path.basename(archive_path).split('.')[0]

    # Upload the archive to /tmp/ on the web server
    put(archive_path, '/tmp/')

    # Create the release folder if it doesn't exist
    sudo('mkdir -p /data/web_static/releases/{}'.format(archive_filename))

    # Uncompress the archive to /data/web_static/releases/
    sudo('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
        archive_filename + '.tgz', archive_filename))

    # Delete the uploaded archive
    sudo('rm /tmp/{}'.format(archive_filename + '.tgz'))

    # Delete the existing symbolic link
    sudo('rm /data/web_static/current')

    # Create a new symbolic link to the new version
    sudo('ln -s /data/web_static/releases/{} /data/web_static/current'.format(
        archive_filename))

    return True
