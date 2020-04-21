from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


from.loadData import loadData
# Create your views here.


def login(request):
    return render(request, 'registration/login.html', {})


def home(request):
    return render(request, 'home.html', {})
   


    


def about(request):
    return render(request, 'about.html', {})




def dashboard(request):
    return render(request, 'dashboard/dashboardPage.html', {})


def fetchDashboardData(request):
   # import requests
    import json

    if request.is_ajax():
        print(request.POST)
        data = json.loads(request.body)




        jsonData = json.dumps({'this' : 'Worked', 'Yes' : 'It fucking worked'})
    return HttpResponse(jsonData, status=200)



