"""
Connection - management class for connection to docker host.
"""

import socket

def host_is_available(hostname):
    try:
        socket_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_host.settimeout(1)
        host, port = (hostname).split(":")
        socket_host.connect((host, int(port)))
        socket_host.close()
        return True
    except socket.error:
        return False