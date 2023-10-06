#!/usr/bin/python3
"""
This Fabric script cleans up old archives on web servers.
"""

from fabric.api import env, local, run
from os.path import exists
from datetime import datetime

env.hosts = ["54.236.30.173", "100.26.56.25"]


def do_clean(number=0):
    """
    Delete outdated archives on both web servers.

    Args:
        number (int): The number of archives to keep.

    Returns:
        None
    """
    if number == 0:
        number = 1
    number = int(number)

    # List all archives in the versions folder on the local machine
    local_archives = local("ls -1t versions", capture=True)

    # List all archives in the /data/web_static/releases folder on the remote servers
    remote_archives = run("ls -1t /data/web_static/releases")

    # Ensure that the archives on both local and remote are not empty
    if local_archives and remote_archives:
        local_archives = local_archives.split("\n")  # Convert to a list
        remote_archives = remote_archives.split("\n")  # Convert to a list

        # Keep only the specified number of archives
        archives_to_keep = local_archives[:number]

        # Delete archives from the local machine that should be removed
        for archive in local_archives[number:]:
            local("rm -f versions/{}".format(archive))

        # Delete archives on the remote servers that should be removed
        for server in env.hosts:
            for archive in remote_archives:
                if archive not in archives_to_keep:
                    run("rm -rf /data/web_static/releases/{}".format(archive))

        print("Old archives removed.")
    else:
        print("No archives to remove.")

if __name__ == "__main__":
    # Set the number of archives to keep
    number_to_keep = 2  # Modify this number as needed

    # Call the do_clean function
    do_clean(number_to_keep)
