from django.db import models

# Create your models here.
class dengon(models.Model):
    name = models.CharField('Name', max_length=255)
    category = models.CharField('Category', max_length=255, blank=True)