from django import forms
from .models import TableStockData

class edit_form(forms.ModelForm):
    class Meta:
        model = TableStockData
        fields = ["date", "trade_code", "high", "low", "open", "close", "volume"]
