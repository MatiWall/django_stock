from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView




app_name = 'accounts'


urlpatterns = [
    path('login/', views.userLogin, name = "login"),
    path('signup/', views.userSignup, name = "signup"),
    path('logout/', views.userLogout, name = "logout"),
    path('profile/', views.userProfile, name = "profile" ),
     path('profile/<int:pk>/', views.userProfile, name = "profile_with_pk" ),
    path('profile/edit/', views.userProfileEdit, name = "editProfile"),
    path('profile/changePassword/', views.userChangePassword, name = 'changePassword'),
    path('profile/resetPassword/', PasswordResetView.as_view( email_template_name = 'accounts/resetPasswordEmail.html', success_url = '/accounts/profile/resetPassword/done/'), name = 'password_reset'),
    path('profile/resetPassword/done/', PasswordResetDoneView.as_view( template_name = 'accounts/resetPasswordDone.html'), name = 'password_reset_done'),
    path('profile/resetPassword/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url = '/accounts/profile/resetPassword/complete/'), name = 'password_reset_confirm'),
    path('profile/resetPassword/complete/', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),

]

# template_name = 'accounts/resetPassword.html'