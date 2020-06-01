from django.urls import path, reverse_lazy
from . import views
from .views import homeView




app_name = 'portfolio'

urlpatterns = [
    path('home/', homeView.as_view(), name = "home"),
]
