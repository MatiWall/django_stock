from django.urls import path, reverse_lazy
from . import views
from . import ajax_views
from .views import homeView




app_name = 'portfolio'

urlpatterns = [
    path('home/', homeView.as_view(), name = "home"),
    path('positions/ajax/', ajax_views.position_view, name = 'positions')
]
