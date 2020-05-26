from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required


app_name = 'dashboard'

urlpatterns = [
    path('dashboard', views.dashboard, name = "dashboard"),
    path('save/', views.save, name = 'save'),
    path('getData/', views.fetchData, name = 'fetchData'),
    path('load/', views.load, name = 'load'),
]

