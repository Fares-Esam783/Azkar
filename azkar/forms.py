from django import forms
from .models import Dhikr

class DhikrForm(forms.ModelForm):
    
    class Meta:
        model = Dhikr
        fields = ['text', 'category']

        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'category': forms.Select(attrs={'class':'form-control'})
        }
