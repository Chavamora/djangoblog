from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    class Meta:
        app_label = 'tasks' 

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.nombre
    
    def snippet(self):
        return self.descripcion[:50] + "..."

class Task(models.Model):
    URGENCIA_CHOICES = [
        ('Urgente', 'Urgente'),
        ('No_Urgente', 'No Urgente'),
    ]
    
    IMPORTANCIA_CHOICES = [
        ('Importante', 'Importante'),
        ('No_Importante', 'No Importante'),
    ]

    titulo = models.CharField(max_length=100)
    notas = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField()
    hora_comienzo = models.TimeField(blank=True, null=True)
    hora_limite = models.TimeField(blank=True, null=True)
    urgencia = models.CharField(max_length=10, choices=URGENCIA_CHOICES)
    importancia = models.CharField(max_length=15, choices=IMPORTANCIA_CHOICES)
    id_lista = models.ForeignKey(TaskList,on_delete=models.PROTECT, default=None, null=True, blank=True)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User,on_delete=models.PROTECT, default=None)
    # python manage.py makemigrations
    # python manage.py migrate

    def __str__(self):
        return self.titulo
    
    def snippet(self):
        return self.notas
