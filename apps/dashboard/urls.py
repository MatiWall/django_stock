from django.urls import path
from . import views, createChart_views

from django.contrib.auth.decorators import login_required


app_name = 'dashboard'

urlpatterns = [
    path('dashboard', views.dashboard, name = "dashboard"),
    path('save/', views.save, name = 'save'),
    path('load/', views.load, name = 'load'),

    path('getHistoricalStockData/', views.getHistoricalStockData, name = 'historicalStockData'),

    path('createChart/', createChart_views.popup, name = 'createChartPopup')
]

