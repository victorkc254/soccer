from django.conf.urls import url
from django.shortcuts import render, redirect
from django.http import HttpResponse, response

import requests
# Create your views here.

def index(request):
    url= "https://apiv3.apifootball.com/?action=get_events&league_id=1&from=2021-07-02&to=2021-10-02&APIkey=f3d7dbc2ccd4f3c48142580d04f58f6f61f615306ee07dba0b231a3a7b251285"
    response = requests.get(url)
    jsonResponse = response.json()
    return render(request,'blog/index.html',{'jsonResponse':jsonResponse})

def specific(request):
    return HttpResponse("list1")
