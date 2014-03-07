from django.contrib import admin
from Informatica.models import *
from Informatica.instance_models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Snapshot)
admin.site.register(InstanceDef)
admin.site.register(InstanceProvider)
admin.site.register(FileInstance)
