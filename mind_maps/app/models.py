from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, null=True)
    birthday = models.DateTimeField(auto_now_add=True)
    deathday = models.DateTimeField(auto_now=False)
    placebirthday = models.CharField(max_length=255, null=True)
    ptoho = models.ImageField(upload_to='media/%Y/%M/%D')
    status = models.BooleanField(null=True)
    is_published = models.BooleanField(default=True)

class Questions(models.Model):
    question = models.TextField(null=True)