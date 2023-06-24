from django import forms
from . import models

class CreateDairy_Entry(forms.ModelForm):
    MOOD_CHOICES = (
        ('feliz', '😊'),
        ('triste', '😢'),
        ('enojado', '😡'),
        ('sorprendido', '😮'),
        ('confundido', '😕'),
    )
    
    mood = forms.ChoiceField(choices=MOOD_CHOICES, label='¿Cómo te sientes?')


    class Meta:
        model = models.Dairy_Entry
        fields = ['titulo', 'cuerpo', 'mood']