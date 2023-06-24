from django import forms
from .models import Task, TaskList

class CreateTask(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        current_list_id = kwargs.pop('current_list_id', None)
        author = kwargs.pop('author', None)  # Obtén el usuario actual de los argumentos
        super(CreateTask, self).__init__(*args, **kwargs)
        self.fields['id_lista'].initial = current_list_id
        
        # Actualiza el queryset del campo 'id_lista' para limitar las opciones al usuario actual
        self.fields['id_lista'].queryset = TaskList.objects.filter(author=author)

    class Meta:
        model = Task
        fields = ['titulo', 'notas', 'fecha_limite', 'hora_comienzo', 'hora_limite', 'urgencia', 'importancia', 'id_lista']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
            'hora_comienzo': forms.TimeInput(attrs={'type': 'time', 'required': False}),
            'hora_limite': forms.TimeInput(attrs={'type': 'time', 'required': False}),
        }


class CreateTaskList(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['nombre', 'descripcion', 'fecha_limite']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }