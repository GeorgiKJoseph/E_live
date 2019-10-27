from django.db import models
from django.conf import settings
from django.utils import timezone

class Component_data(models.Model):
    name = models.CharField(max_length=40)
    typ = models.CharField(max_length=40)
    room = models.CharField(max_length=40)
    watt = models.IntegerField()

class Component_status(models.Model):
    cid = models.ForeignKey(Component_data,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    last_update_time = models.DateTimeField(default=timezone.now)

class home(models.Model):
    total_energy_consumed = models.IntegerField()

class history:
    month = models.DateTimeField(default=timezone.now)
    bill_amount = models.IntegerField()
    total_energy_consumed = models.IntegerField()

