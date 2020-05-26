from django.urls import path
from . import views


app_name = 'notes'

urlpatterns = [
    path(r'/home/', views.home, name = 'notesHome'),
]
