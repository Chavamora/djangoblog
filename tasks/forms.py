from django import forms
from .models import Task, TaskList

class CreateTask(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        current_list_id = kwargs.pop('current_list_id', None)
        super(CreateTask, self).__init__(*args, **kwargs)
        self.fields['id_lista'].initial = current_list_id

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