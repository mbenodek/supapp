from django.shortcuts import render
from django.http import HttpResponse
from .models import information

# Create your views here.


def index(request):
    personalInfo = information.objects.all()
    return render(request, 'index.html', {'info': personalInfo})
