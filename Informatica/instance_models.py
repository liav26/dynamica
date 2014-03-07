from Informatica.models import InstanceBase
from django.db import models

class FileInstance(InstanceBase):
    filename = models.TextField(max_length=512)
    checksum = models.TextField(max_length=32)

