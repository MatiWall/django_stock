from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse

from django.db import connection

from .forms import homeForm
from .models import post, friend

#from django.http import HttpResponse, JsonResponse

#from django.db import connection, transaction


#from.loadData import loadData
from .webscraping import yhaooWebscraping, stockScreener

#from iexfinance.stocks import Stock, get_historical_data
#from datetime import datetime

#import json
#import os


from django.views.generic import TemplateView
# Create your views here.

'''
def home(request):
 
    currencyUrl = 'https://finance.yahoo.com/currencies?.tsrc=fin-srch'
    currency = yhaooWebscraping(currencyUrl)
    currencyData = currency.get_html()


    cryptoUrl = 'https://finance.yahoo.com/cryptocurrencies?.tsrc=fin-srch'
    crypto = yhaooWebscraping(cryptoUrl)
    cryptoData = crypto.get_html()

    commodityUrl = 'https://finance.yahoo.com/commodities?.tsrc=fin-srch'
    commodity = yhaooWebscraping(commodityUrl)
    commodityData = commodity.get_html()



    tsla = stockScreener(['TSLA'])
    tsla.scrapeStocks()
    



    return render(request, 'home.html', {'currency' : currencyData ,'crypto' : cryptoData, 'commodity' : commodityData})
   '''

class homeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = homeForm()

        posts = post.objects.all().order_by('-created')
        users = User.objects.exclude(id = request.user.id)

        
        try:
            Friend = friend.objects.get(current_user = request.user)
            friends = Friend.users.all()
        except:
            friends = None
    
        args = {'form': form, 'posts': posts, 'users': users, 'friends': friends}

        return render(request, self.template_name, args)

    def post(self, request):
        form = homeForm(request.POST)
    
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            return redirect('about')


        return render(request, self.template_name, {'form': form, 'text' : text})




    



class aboutView(TemplateView):
    template_name = 'about.html'
    #return render(request, self.template_name, {})



def changeFriends(request, operation, pk):
    newFriend = User.objects.get(pk = pk)

    if operation == 'add':
        friend.make_friend(request.user, newFriend)
    elif operation == 'remove':
        friend.lose_friend(request.user, newFriend)
    


    return redirect('home')


