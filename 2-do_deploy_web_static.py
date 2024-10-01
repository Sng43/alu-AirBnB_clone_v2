#!/usr/bin/python3
"""
A Fabric script that creates and distributes an archive to your web servers.

This script allows you to deploy a web application archive to specified web servers.
It checks if the archive exists, uploads it to the server, and extracts it into the correct directory.
"""

import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

# Define the host servers for deployment
env.hosts = ["3.88.187.103", "3.87.94.49"]

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    This function takes the path of an archive file, checks if it exists,
    uploads it to a remote server, and extracts it to the appropriate location.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: 
            - False if the file doesn't exist at `archive_path` or if an error occurs during the process.
            - True if the deployment is successful.

    Steps:
        1. Check if the archive exists at the specified `archive_path`.
        2. Extract the filename and name (without extension) from the archive path.
        3. Upload the archive to the remote server's temporary directory.
        4. Remove any existing release folder for the application on the server.
        5. Create a new directory for the application release.
        6. Extract the uploaded archive into the new release directory.
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
