from django.db import models
from django.conf import settings

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class HorseTour(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class TourRegistration(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    tour = models.ForeignKey(HorseTour,on_delete=models.PROTECT)
    location = models.ForeignKey(Location,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.tour} ({self.location})"

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ClothesModel(models.Model):
    title = models.CharField(max_length=100)
    brands_name = models.ManyToManyField(Brand)
    image = models.ImageField(upload_to='clothes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-----{', '.join(i.name for i in self.brands_name.all() )}'