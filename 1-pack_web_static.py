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
from datetime import datetime
import tarfile


def do_pack():
    """
    Generate a .tgz archive of web_static and store it in the versions folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        # Generate archive name based on current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Create the 'versions' directory if it doesn't exist
        if not os.path.exists("versions"):
            os.mkdir("versions")

        # Compress the 'web_static' directory into a .tgz archive
        with tarfile.open(
            "versions/{}".format(archive_name),
            "w:gz"
        ) as archive:
            archive.add("web_static", arcname=os.path.basename("web_static"))

        # Return the path to the archive
        return "versions/{}".format(archive_name)
    except Exception:
        return None

if __name__ == "__main__":
    result = do_pack()
    if result:
        print("Archive created:", result)
    else:
        print("Archive creation failed.")
