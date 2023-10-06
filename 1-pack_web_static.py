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

import os
from fabric.api import local
from datetime import datetime
import tarfile


def do_pack():
    """
    Generate a .tgz archive of web_static and store it in the versions folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
