from django.db import models
from Informatica import config

# Create your models here.

class Profile(models.Model):
    name = models.TextField(max_length=config.MAX_NAME_LENGTH)

class InstanceDef(models.Model):
    name = models.TextField(max_length=config.MAX_NAME_LENGTH)

class InstanceBase(models.Model):
    __date_created__ = models.DateTimeField(auto_now_add=True)
    __def__ = models.ForeignKey('InstanceDef', related_name='+')


class InstanceProvider(models.Model):
    instance_def = models.ForeignKey('InstanceDef', related_name='provider')

class Snapshot(models.Model):
    snap_id = models.IntegerField(primary_key=True)
    date_started = models.DateTimeField()
    date_taken = models.DateTimeField(auto_now_add = True)
    provider = models.ForeignKey('InstanceProvider', related_name='snapshots')

