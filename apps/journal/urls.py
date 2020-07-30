from django.urls import path
from . import views



app_name = 'journal'


urlpatterns = [
    path('dashboard/', views.dashboardView.as_view(), name = "dashboard"),
    path('trades/', views.tradesView.as_view(), name = "trades"),


]
