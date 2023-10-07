#!/usr/bin/python3
"""
This Fabric script deploys an archive to web servers.
"""

import os.path
from datetime import datetime
from fabric.api import *

env.user = "ubuntu"
env.hosts = ["54.236.30.173", "100.26.56.25"]
env.key_filename = "~/id_rsa"


def do_deploy(archive_path):
    """
    Distribute an archive to web servers and update the current symlink.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    try:
        if not (os.path.exists(archive_path)):
            return False

        put(archive_path, '/tmp/')

        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'.format(timestamp))

        run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'.format(timestamp))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/web_static_{}/ /data/web_static/current'.format(timestamp))
    except:
        return False

    return True
