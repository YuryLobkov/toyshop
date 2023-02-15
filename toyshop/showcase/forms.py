from django import forms
from .models import Customer


class PurchaseForm(forms.ModelForm):
    model = Customer
    fields = ['email',
              'first_name',
              'last_name',
              'purchase']


class OrderForm(forms.ModelForm):
    model = Customer
    fields = ['email',
              'first_name',
              'last_name',
              'order']