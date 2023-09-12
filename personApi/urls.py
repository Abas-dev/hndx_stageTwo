from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('create/',views.CreatePerson.as_view(),name='create'),
    path('get/',views.GetAllPerson.as_view(),name='getPerson'),
    path('byId/<int:pk>',views.GetUpdateDeletePerson.as_view(),name='byId')
]