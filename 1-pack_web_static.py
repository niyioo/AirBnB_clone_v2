#!/usr/bin/python3
"""
This script generates a .tgz archive from the
contents of the web_static folder.

All files in the folder web_static must be added to the final archive.
All archives must be stored in the folder versions.
The name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz.
The function do_pack must return the archive path if the
archive has been correctly generated. Otherwise, it should return None.
"""

import os.path
from fabric.api import local
from datetime import datetime
import tarfile
import re


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
