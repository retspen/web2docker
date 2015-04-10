"""
Connection - management class for connection to docker host.
"""

from docker import Client
from docker.tls import TLSConfig

SOCKET = 1
SIMPLE = 2
TLS_PUB_TRUE = 3
TLS_PUB_FALSE = 4
TLS_CA = 5
TLS_USER_WITHOUT_CA = 6
TLS_USER_WITH_CA = 7


class dkrConnection(object):

    def __init__(self, hostname, conn_type, tlsuser=None, tlskey=None, tlsca=None):
        # connection objects
        self.hostname = hostname
        self.conn_type = conn_type
        self.tlsuser = tlsuser
        self.tlskey = tlskey
        self.tlsca = tlsca

    def connect(self):
        if self.conn_type == SOCKET:
            self.conn = Client(base_url='unix://var/run/docker.sock')

        if self.conn_type == SIMPLE:
            self.conn = Client(base_url='tcp://' + self.hostname)

        if self.conn_type == TLS_PUB_TRUE:
            self.conn = Client(base_url='https://' + self.hostname, tls=True)

        if self.conn_type == TLS_PUB_FALSE:
            tls_config = TLSConfig(verify=False)
            self.conn = Client(base_url='https://' + self.hostname,
                               tls=tls_config
                               )

        if self.conn_type == TLS_CA:
            tls_config = TLSConfig(ca_cert=self.tlsca)
            self.conn = Client(base_url='https://' + self.hostname,
                               tls=tls_config
                               )

        if self.conn_type == TLS_USER_WITHOUT_CA:
            tls_config = TLSConfig(client_cert=(self.tlsuser, self.tlskey))
            self.conn = Client(base_url='https://' + self.hostname,
                               tls=tls_config
                               )

        if self.conn_type == TLS_USER_WITH_CA:
            tls_config = TLSConfig(client_cert=(self.tlsuser, self.tlskey),
                                   verify=self.tlsca
                                   )
        return self.conn
