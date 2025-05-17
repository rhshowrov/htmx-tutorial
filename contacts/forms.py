from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
class ContactForm(forms.ModelForm):
    name=forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'input w-full',
            'placeholder':'Contact name'
        })
    )
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'input w-full',
            'placeholder':'Contact Email'
        })
    )
    
    def clean_name(self):
        name=self.cleaned_data['name']
        if not name or not name[0].isalpha():
            raise ValidationError('Name must be start with a letter')
        return name
    
    def clean_email(self):
        email=self.cleaned_data['email']
        if Contact.objects.filter(user=self.initial.get('user',None),email=email).exists():
            raise ValidationError('Email exist within your saved contacts')
        return email

    class Meta:
        model=Contact
        fields=('name','email')
