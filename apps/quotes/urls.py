from django.urls import path
from . import views
from .views import aboutView, homeView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', homeView.as_view(), name = "home"),
    path('connect/<str:operation>/<int:pk>/', views.changeFriends, name = 'changeFriends'),
    path('about/', aboutView.as_view(), name = "about"),
]
