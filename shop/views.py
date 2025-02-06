from django.shortcuts import render
# from django.http import HttpResponse
from .models import Desideorio

def index(request):
    desideorios =Desideorio.objects.all()
    return render(request, 'desideorios.html')