from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

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
    path('userProfile/', views.userProfile, name = "profile" ),
    path('userProfile/edit/', views.userProfileEdit, name = "editProfile"),
    path('userProfile/changePassword/', views.userChangePassword, name = 'changePassword'),
    path('userProfile/resetPassword/', PasswordResetView.as_view(), name = 'password_reset'),
    path('userProfile/resetPassword/done/', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('userProfile/resetPassword/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('userProfile/resetPassword/complete/', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
]