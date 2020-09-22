from django import forms
from .models import Session


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['user', 'name', 'description', 'cards', 'access', 'access_code']
        widgets = {
            'user': forms.HiddenInput()
        }
