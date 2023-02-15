from django import forms
from .models import Order


class PurchaseForm(forms.ModelForm):
    model = Order
    fields = [
        'email',
        'customer_name',
        'phone_number',
        'preferable_messenger',
        'order_new',
        'comment',
    ]


class OrderForm(forms.ModelForm):
    model = Order
    fields = [
        'email',
        'customer_name',
        'phone_number',
        'preferable_messenger',
        'comment',
    ]
