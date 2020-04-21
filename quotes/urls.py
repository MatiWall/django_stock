from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login, name = "login"),
    path('about/', views.about, name = "about"),
    path('dashboard/', views.dashboard, name = "dashboardPage"),
    path('dashboard/getData/', views.fetchDashboardData, name = 'getDashboardData'),
]
