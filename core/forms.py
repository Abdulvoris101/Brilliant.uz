# forms.py

from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'phone_number', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'flex: 1'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'flex: 1', 'placeholder': '97722xxxx'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }

