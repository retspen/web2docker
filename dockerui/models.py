from django.db import models


class Server(models.Model):
    description = models.CharField(max_length=255)
    hostname = models.CharField(max_length=20)
    conn_type = models.IntegerField(max_length=1)

    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Servers"

    def __str__(self):
        return self.description


class CertFiles(models.Model):
    description = models.CharField(max_length=50)
    server = models.ForeignKey(Server)
    tlscert = models.CharField(max_length=255)
    tlskey = models.CharField(max_length=255)
    tlscacert = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"

    def __str__(self):
        return self.description
