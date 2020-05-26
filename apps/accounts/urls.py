from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


app_name = 'accounts'


urlpatterns = [
    path('login/', views.userLogin, name = "login"),
    path('signup/', views.userSignup, name = "signup"),
    path('logout/', views.userLogout, name = "logout"),
    path('profile/', views.userProfile, name = "profile" ),
    path('profile/edit/', views.userProfileEdit, name = "editProfile"),
    path('profile/changePassword/', views.userChangePassword, name = 'changePassword'),
    path('profile/resetPassword/', PasswordResetView.as_view(), name = 'password_reset'),
    path('profile/resetPassword/done/', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('profile/resetPassword/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('profile/resetPassword/complete/', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),

]