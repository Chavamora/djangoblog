from django import forms
from . import models

class CreateHobbie(forms.ModelForm):
    class Meta:
        model = models.Hobbie
        fields = ['titulo', 'cuerpo', 'slug']

    