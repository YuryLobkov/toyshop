from django import forms
from .models import Order


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'email',
            'customer_name',
            'phone_number',
            'preferable_messenger',
            'comment',
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'email',
            'customer_name',
            'phone_number',
            'preferable_messenger',
            'comment',
        ]
