
from django.contrib import admin
from . import models

admin.site.register(models.Brand)
admin.site.register(models.ClothesModel)

admin.site.register(models.Location)
admin.site.register(models.HorseTour)
admin.site.register(models.TourRegistration)