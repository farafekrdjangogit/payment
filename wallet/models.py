from django.db import models
from django.utils import timezone

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    basket_id = models.FloatField(default=0,)
    ip = models.CharField(max_length=200)
    keycode = models.CharField(max_length=200, blank=True, null=True),
    amount = models.FloatField(default=0,)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)
    bankcode = models.CharField(max_length=200),
    paid = models.IntegerField(default=0,)
    bankau = models.CharField(max_length=200)
