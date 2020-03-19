from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login, name = "login"),
    path('about/', views.about, name = "about"),
    path('addStock/', views.addStock, name = "addStock"),
    path('delete/<stockId>', views.delete, name="delete"),
     path('dashboard/', views.dashboard, name = "dashboardPage"),
]
