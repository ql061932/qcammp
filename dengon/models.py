from django.db import models
from django.utils import timezone

# Create your models here.
class dengon(models.Model):
    id = models.AutoField(primary_key=True)
    nameTo = models.CharField(max_length=50, default='')
    mailTo = models.EmailField(max_length=100, default='')
    nameFrom = models.CharField(max_length=50, default='')
    nameTakenBy = models.CharField(max_length=50, default='')
    mailTakenBy = models.EmailField(max_length=100, default='')
    dateTime = models.DateTimeField(default=timezone.now)
    requirement = models.IntegerField(default=0)
    phoneNumber = models.CharField(max_length=50, default='')
    message = models.TextField(default='')
    check = models.BooleanField(default=False)
