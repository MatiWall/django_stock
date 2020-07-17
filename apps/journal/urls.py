from django.urls import path
from . import views
from . import ajax_views


app_name = 'journal'


urlpatterns = [
    path('home/', views.homeView.as_view(), name = "home"),
    path('dashboard/', views.dashboardView, name = "dashboard"),
    path('trades/', views.tradesView.as_view(), name = 'trades'),
    path('edit/', views.editView.as_view(), name = "edit"),


    path('getUserJournals/', ajax_views.homeTableView.as_view(), name = 'homeTableData'),
    path('postJournalEntry/', ajax_views.journalFormView, name = 'postJournalEntry'),
]
