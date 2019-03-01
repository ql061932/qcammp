from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from dengon.models import Check_list

def init(request):
    entities = Check_list.objects.all()
    html = render_to_string('index.html', {'entities':entities})     
    return HttpResponse(html)


def add_task(request):     
    name = request.GET['name']     
    category = request.GET['category']
    Check_list.objects.update_or_create(name=name,category=category)
    entities = Check_list.objects.all()   
    html = render_to_string('list.html', {'entities':entities})     
    return HttpResponse(html)