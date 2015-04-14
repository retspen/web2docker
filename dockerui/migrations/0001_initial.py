# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=50)),
                ('tlscert', models.CharField(max_length=255)),
                ('tlskey', models.CharField(max_length=255)),
                ('tlscacert', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('hostname', models.CharField(max_length=20)),
                ('conn_type', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Host',
                'verbose_name_plural': 'Hosts',
            },
        ),
        migrations.AddField(
            model_name='certfiles',
            name='host',
            field=models.ForeignKey(to='dockerui.Host'),
        ),
    ]
