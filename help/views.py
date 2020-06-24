from django.shortcuts import render
from django.http import HttpResponse
from .models import information
from caronainfo import stats
import requests


# Create your views here.


def index(request):
    return render(request, 'index.html')


def info(request):
    return render(request, 'info.html')


def tracker(request):
    # get the list of todos
    response = requests.get('http://covid-19india-api.herokuapp.com/all')
    # transfor the response to json objects
    india_count = response.json()
    print(india_count)
    return render(request, 'tracker.html', {'india_count': india_count})

    # india_count = stats.get_info_label()
    #return render(request, 'tracker.html', {'india_count': india_count})
    #return HttpResponse("testing")

def life(request):
    personalInfo = information.objects.all()
    return render(request, 'life.html', {'info': personalInfo})

