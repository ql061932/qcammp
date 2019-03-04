from django.db import models
from django.utils import timezone

# Create your models here.
class dengon(models.Model):
    id = models.AutoField(primary_key=True)
    nameTo = models.CharField(max_length=255, default='')
    nameFrom = models.CharField(max_length=255, default='')
#    takenBy = models.CharField('takenBy', max_length=255)
#    dateTime = models.DateTimeField(default=timezone.now)
#    Requirement = models.CharField('Requirement', max_length=255)
#    phoneNumber = models.CharField('phoneNumber', max_length=255)
#    Message = models.CharField('Message', max_length=255)
