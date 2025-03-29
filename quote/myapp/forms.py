from django import forms
from .models import React

class QuoteForm(forms.ModelForm):
    class Meta:
        model = React
        fields = ['name', 'detail']
