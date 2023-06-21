from django import forms
from . import models

class CreateDairy_Entry(forms.ModelForm):
    class Meta:
        model = models.Dairy_Entry
        fields = ['titulo', 'cuerpo']