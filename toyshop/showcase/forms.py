from django import forms
from .models import Order, Toy
from django.utils.translation import gettext_lazy as _


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
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':_('example@mail.com')}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':_('Jane Joe')}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':_('+995999999999')}),
            'preferable_messenger': forms.RadioSelect(attrs={'class': ''}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder':_('Let us know details for you order')})
            }


    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = _("Your email")
        self.fields['customer_name'].label = _("Your name")
        self.fields['phone_number'].label = _("Phone number")
        self.fields['preferable_messenger'].label = _("How can we comunicate")
        self.fields['comment'].label = _("Comments for your order")


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
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':_('example@mail.com')}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':_('Jane Joe')}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':_('+995999999999')}),
            'preferable_messenger': forms.RadioSelect(attrs={'class': ''}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder':_('Please describe what kind of toy you want, and I will contact you to clarify details')})
            }


    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = _("Your email")
        self.fields['customer_name'].label = _("Your name")
        self.fields['phone_number'].label = _("Phone number")
        self.fields['preferable_messenger'].label = _("How can we comunicate")
        self.fields['comment'].label = _("Comments for your order")

class FilterShowcaseForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = [
            'material',
            'size',
            'category',
            'in_stock',
        ]
        widgets = {
            'material': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'in_stock': forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch'}),
        }

    def __init__(self, initials, *args, **kwargs):
        super(FilterShowcaseForm, self).__init__(*args, **kwargs)
        self.fields['material'].empty_label = _("--All materials--")
        self.fields['size'].empty_label = _("--All sizes--")
        self.fields['category'].empty_label = _("--All categories--")
        # TODO refactor below in one line using "update(zip)" https://stackoverflow.com/questions/54868711/python-set-list-elements-as-dict-values
        self.initial['material'] = initials[0]
        self.initial['size'] = initials[1]
        self.initial['category'] = initials[2]
        self.initial['in_stock'] = initials[3]        
        for field in self.fields.values():
            field.required = False
