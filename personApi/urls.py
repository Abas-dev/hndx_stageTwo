from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('create/',views.CreatePerson.as_view(),name='create'),
    
]