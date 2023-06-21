from django.urls import path
from . import views

app_name = 'dairy'

urlpatterns = [
    path('', views.dairy_entry_list, name="list"),
    path('create/', views.dairy_entry_create, name="create"),
    path('<id>/', views.dairy_entry_details, name="detail"),
    
]
