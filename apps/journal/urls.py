from django.urls import path
from . import views
from . import ajax_views


app_name = 'journal'


urlpatterns = [
    path('dashboard/', views.dashboardView.as_view(), name = "dashboard"),
    path('trades/', views.tradesView.as_view(), name = "trades"),
    path('trades/detail/', views.tradeDetailView.as_view(), name = 'tradeDetail'),
    path('edit/', views.editView.as_view(), name = "edit"),


    path('newEntry/', ajax_views.journalEntryCreateView.as_view(), name = 'createJournalEntry'),

    path('getUserJournals/', ajax_views.homeTableView.as_view(), name = 'homeTableData'),
    path('postJournalEntry/', ajax_views.journalFormView, name = 'postJournalEntry'),
]
