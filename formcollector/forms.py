from django import forms
from .models import FormEntry

class DataEntryForm(forms.ModelForm):
    second_field = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = FormEntry
        fields = ['first_field', 'second_field']

