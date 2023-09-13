from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('',views.CreatePerson.as_view(),name='create'),
    path('<int:pk>',views.GetUpdateDeletePerson.as_view(),name='byId')
]