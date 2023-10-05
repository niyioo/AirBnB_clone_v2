#!/usr/bin/python3
"""
This Fabric script deploys an archive to web servers.
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os

# Specify the SSH user and web server IP addresses
env.user = 'ubuntu'
env.hosts = ['54.236.30.173', '100.26.56.25']


def deploy():
    """
    Deploy the web_static content to the web servers.
    """
    archive_path = do_pack()

    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
