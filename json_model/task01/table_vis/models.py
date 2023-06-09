from django.db import models

class table_vis(models.Model):
    date = models.CharField(max_length=100)
    trade_code = models.CharField(max_length=100)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.CharField(max_length=100)

