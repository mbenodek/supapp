from django.shortcuts import render
from django.http import HttpResponse
from .models import information
from caronainfo import stats

# Create your views here.


def index(request):
    return render(request, 'index.html')


def info(request):
    return render(request, 'info.html')


def tracker(request):
    india_count = stats.get_info_label()
    return render(request, 'tracker.html', {'india_count': india_count})

def life(request):
    personalInfo = information.objects.all()
    return render(request, 'life.html', {'info': personalInfo})

