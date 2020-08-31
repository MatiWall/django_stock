from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('portfolios', views.portfolioView, basename = 'portfolio')

router.register('journals', views.journalView, basename = 'journal')

router.register('journalActions', views.journalActionView, basename = 'journal-action')
router.register('journalTargets', views.journalTargetView, basename = 'journal-target')


app_name = 'journal-api'
print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
    path('portfolio/form/', views.portfolioFormView.as_view(), name = 'portfolioForm'),
    path('journal/form', views.journalFormView.as_view(), name = 'journalForm'),

]