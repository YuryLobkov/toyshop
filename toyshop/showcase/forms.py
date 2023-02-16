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
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'example@mail.com'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Jane Joe'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'+995999999999'}),
            'preferable_messenger': forms.RadioSelect(attrs={'class': ''}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Let us know details for you order'})
            }


    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Your email"
        self.fields['customer_name'].label = "Your name"
        self.fields['phone_number'].label = "Phone number"
        self.fields['preferable_messenger'].label = "How can we comunicate"
        self.fields['comment'].label = "Comments for your order"


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
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'example@mail.com'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Jane Joe'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'+995999999999'}),
            'preferable_messenger': forms.RadioSelect(attrs={'class': ''}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Please describe what kind of toy you want, and I will contact you to clarify details'})
            }


    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Your email"
        self.fields['customer_name'].label = "Your name"
        self.fields['phone_number'].label = "Phone number"
        self.fields['preferable_messenger'].label = "How can we comunicate"
        self.fields['comment'].label = "Comments for your order"
