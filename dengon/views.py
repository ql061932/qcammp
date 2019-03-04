# coding: UTF-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from dengon.models import dengon

def input(request):
    entities = dengon.objects.all()
    return render(request, 'input.html', {'entities':entities});

def list(request):     
    nameTo = request.POST['nameTo']
    nameFrom = request.POST['nameFrom']
    dengon.objects.update_or_create(nameTo=nameTo,nameFrom=nameFrom)
    entities = dengon.objects.all()
    return render(request, 'list.html', {'entities':entities});
