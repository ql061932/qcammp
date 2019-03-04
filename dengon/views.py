from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from dengon.models import dengon

def input(request):
    entities = dengon.objects.all()
    html = render_to_string('input.html', {'entities':entities})     
    return HttpResponse(html)


def list(request):     
    name = request.GET['name']     
    category = request.GET['category']
    dengon.objects.update_or_create(name=name,category=category)
    entities = dengon.objects.all()   
    html = render_to_string('list.html', {'entities':entities})     
    return HttpResponse(html)