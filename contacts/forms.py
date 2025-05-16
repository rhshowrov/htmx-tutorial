from django import forms
from .models import Contact
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

    class Meta:
        model=Contact
        fields=('name','email')
