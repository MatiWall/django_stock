from django.urls import path
from . import views


app_name = 'notes'

urlpatterns = [
    path('home/', views.home.as_view(), name = 'home'),
    path('task/completed', views.taskCompleted, name = 'taskCompleted'),
    path('save/', views.saveStickyNotes, name = 'save'),
    path('load/', views.getStickyNotes, name = 'load')
]
