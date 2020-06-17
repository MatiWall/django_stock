from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import dashboardComponentOptions



def popup(request):

    DashboardComponentOptions  = dashboardComponentOptions.objects.all()

    return render(request, 'dashboard/createComponentPopup/popupWindow.html', {'DashboardComponentOptions' :  DashboardComponentOptions})





def chartOptions(request, type):

    print(type)
    return HttpResponse('It works')
