from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, null=True)
    birthday = models.DateField(auto_now_add=True)
    deathday = models.DateField(auto_now=False)
    placebirthday = models.CharField(max_length=255, null=True)
    ptoho = models.ImageField(upload_to='photo')
    status = models.BooleanField(null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def get_full_years(self):
        pass

class Questions(models.Model):
    question = models.TextField(null=True)

    def __str__(self):
        return f"{self.question}"

class Post(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')