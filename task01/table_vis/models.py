from django.db import models

class TableStockData(models.Model):
    id = models.TextField(primary_key=True)
    date = models.TextField()  # This field type is a guess.
    trade_code = models.TextField()  # This field type is a guess.
    high = models.TextField()  # This field type is a guess.
    low = models.TextField()  # This field type is a guess.
    open = models.TextField()  # This field type is a guess.
    close = models.TextField()  # This field type is a guess.
    volume = models.TextField()  # This field type is a guess.

    class Meta:
        # managed = False
        db_table = 'table_stock_data'
