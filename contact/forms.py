from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fileds = ("full_name", "email", "phone_number", "massage")