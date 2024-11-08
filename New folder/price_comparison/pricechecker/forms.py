# pricechecker/forms.py
from django import forms

class ProductSearchForm(forms.Form):
    product_name = forms.CharField(max_length=255, label='Enter product name')

