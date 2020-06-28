from django.shortcuts import render
from django.http import HttpResponse
from .models import information
from caronainfo import stats
import requests
import json



# Create your views here.


def index(request):
    headline_resp = requests.get('http://covid-19india-api.herokuapp.com/headlines')
    news = headline_resp.json()
    return render(request, 'index.html', {'news': news})


def info(request):
    return render(request, 'info.html')


def tracker(request):
    # get the list of todos
    india_response = requests.get('http://covid-19india-api.herokuapp.com/all')
    # transfor the response to json objects
    india_count = india_response.json()
    global_count = requests.get('http://covid-19india-api.herokuapp.com/global')
    gcount = json.loads(global_count.text)
    return render(request, 'tracker.html', {'india_count': india_count})

    # india_count = stats.get_info_label()
    #return render(request, 'tracker.html', {'india_count': india_count})
    #return HttpResponse("testing")

def life(request):
    personalInfo = information.objects.all()
    return render(request, 'life.html', {'info': personalInfo})

