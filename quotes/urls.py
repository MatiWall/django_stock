from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('dashboard/', views.dashboard, name = "dashboardPage"),
    path('dashboard/getData/', views.fetchDashboardData, name = 'fetchDashboardData'),
    path('dashboard/saveDashboard/', views.saveDashboard, name = 'saveDashboard'),
    path('dashboard/loadDashboard/', views.loadDashboard, name = 'loadDashboard'),

    path('userLogin/', views.userLogin, name = "login"),
    path('userSignup/', views.userSignup, name = "signup"),
    path('userLogout/', views.userLogout, name = "logout"),
]
