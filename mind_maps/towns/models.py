from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Place(MPTTModel):
    name = models.CharField(max_length=255, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Место(Страна, Регион, Город)'
        verbose_name_plural = 'Место'

    class MPTTMeta:
        order_insertion_by = ['name']