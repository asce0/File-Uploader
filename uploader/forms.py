from django import forms
from .models import Person


class UploadForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = (
            'name',
            'age',
            'email',
            'image',
            'cv'
        )