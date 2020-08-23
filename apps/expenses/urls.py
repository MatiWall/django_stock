from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'expenses'




router = DefaultRouter()
router.register('general', views.userdefiendInputControlView, basename='user-definedinput-control')

print(router.urls)

urlpatterns = [
    path('expenses/', views.home.as_view(), name = "expenses"),
    path('add-expense/', views.addExpense.as_view(), name = 'add-expense'),
    path('edit-expense/<int:pk>', views.editExpense.as_view(), name = 'edit-expense'),
    path('delete-expense/<int:pk>', views.deleteExpense, name = 'delete-expense'),
    path('list-expenses/', views.searchExpensesListView.as_view(), name = 'list-expenses'),
    path('expenses-summary/', views.expensesSummary.as_view(), name = 'expenses-summary'),

    path('expenses-category-summary', views.expensesCategorySummary, name = 'expenses-category-summary'),



    path('income/', views.incomeView.as_view(), name = 'income'),
    path('add-income', views.addIncomeView.as_view(), name = 'add-income'),
    path('delete-income/<str:pk>', views.editIncomeView.as_view(), name = 'edit-income'),
    path('delete-income/<str:pk>', views.deleteIncomeView, name = 'delete-income'),


    path('general/' , views.generalView.as_view(), name = 'general'),
    path('general/userdefined-input/<str:model>', views.userdefinedInputView.as_view(), name = 'userdefined-input'),
    path('general/api/', include(router.urls)),

]

