from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.taskList_list, name="tl_list"),
    path('tasklist/create/', views.taskList_create, name="tl_create"),
    path('tasklist/<id>/', views.taskList_details, name="tl_details"),
    path('tasklist/delete/<id>/', views.taskList_delete, name="tl_delete"),

    path('create/', views.task_create, name="create"),
    path('create/<tlid>', views.task_create, name="createtlid"),
    path('<id>/', views.task_details, name="details"),
    path('delete/<id>/', views.task_delete, name="delete"),
    path('completed', views.task_completed, name="complete"),
]

