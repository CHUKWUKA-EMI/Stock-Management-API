from django.db import models
import uuid

# Create your models here.
class Stock(models.Model):
  name = models.CharField(blank=False, max_length=100)
  currentPrice = models.FloatField(blank=False)
  lastUpdate = models.DateTimeField(auto_now_add=True)