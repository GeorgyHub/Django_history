from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, null=True)
    birthday = models.DateTimeField(null=True)
    deathday = models.DateTimeField()
    placebirthday = models.CharField(max_length=255, null=True)
    ptoho = models.ImageField()
    status = models.BooleanField(null=True)