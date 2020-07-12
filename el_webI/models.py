from django.db import models
from django.conf import settings
from django.utils import timezone


# Switch Board
class Board(models.Model):
    boardNo = models.IntegerField()
    instant_power = models.FloatField()
    def __str__(self):
        return str(self.boardNo)

# Device info
class Component_data(models.Model):
    deviceNo = models.IntegerField()
    boardNo = models.ForeignKey(Board,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=40)
    status = models.BooleanField(default=False)
    current = models.FloatField(default=0.0)
    watt = models.IntegerField()
    last_update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Device_Log_24hr(models.Model):
    dev_id = models.ForeignKey(Component_data,on_delete=models.CASCADE)
    duration = models.IntegerField()
    frequency = models.IntegerField()


class Board_Log_24hr(models.Model):
    boardNo = models.ForeignKey(Board, on_delete=models.CASCADE)
    day = models.DateTimeField(default=timezone.now)
    total_energy_consumed = models.IntegerField()


class history(models.Model):
    month = models.DateTimeField(default=timezone.now)
    bill_amount = models.IntegerField()
    total_energy_consumed = models.IntegerField()
