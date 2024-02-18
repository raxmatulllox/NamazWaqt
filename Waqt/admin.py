from django.contrib import admin

from . import models


# Register your models here.
admin.site.register(models.ProfileModel)
admin.site.register(models.SendMessageModel)
