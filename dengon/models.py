from django.db import models
from django.utils import timezone

# Create your models here.
class dengon(models.Model):
    id = models.AutoField(primary_key=True)
    nameTo = models.CharField(max_length=255, default='')
    nameFrom = models.CharField(max_length=255, default='')
    takenBy = models.CharField(max_length=255, default='')
    dateTime = models.DateTimeField(default=timezone.now)
    requirement = models.CharField(max_length=255, default='')
    phoneNumber = models.CharField(max_length=255, default='')
    message = models.CharField(max_length=255, default='')
