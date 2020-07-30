from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('portfolios', views.portfolioView, basename = 'portfolio')

router.register('journals', views.journalView, basename = 'journal')




app_name = 'journal-api'



urlpatterns = [
    path('', include(router.urls)),
    path('portfolio/form/', views.portfolioFormView.as_view(), name = 'portfolioForm'),
    path('journal/form', views.journalFormView.as_view(), name = 'journalForm')
 
]