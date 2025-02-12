from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Desideorio

def index(request):
    desideorios =Desideorio.objects.all()
    return render(request, 'desideorios.html', {"desideorios": desideorios})

def single_desideorio(request, desideorio_id):
    #Вариант 1
    # try:
    #     desideorio=Desideorio.objects.get(pk=desideorio_id)
    #     return render(request, 'single_desideorio.html', {'desideorio': desideorio})
    # except Desideorio.DoesNotExist:
    #     raise Http404()
    #Вариант 2
    desideorio = get_object_or_404(Desideorio, pk=desideorio_id)
    return render(request, 'single_desideorio.html', {'desideorio': desideorio})