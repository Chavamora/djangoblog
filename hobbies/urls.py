from django.urls import path
from . import views

app_name = 'hobbies'

urlpatterns = [
    path('', views.hobbie_list, name="list"),
    path('create/', views.hobbie_create, name="create"),
    path('<id>/', views.hobbie_details, name="detail"),
    
]
