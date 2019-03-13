# coding: UTF-8
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from dengon.models import dengon
from dengon.forms import dengonForm

def input(request):
	entities = dengon.objects.all()
	return render(request, 'input.html', {'entities':entities})

def list(request):
	#check
	form = dengonForm(request.POST)
	if not form.is_valid():
	    return render(request, 'input.html', {'error':1})
	#create
	if 'nameTo' in request.POST:
		nameTo = request.POST['nameTo']
		nameFrom = request.POST['nameFrom']
		dengon.objects.update_or_create(nameTo=nameTo,nameFrom=nameFrom)
	#search
	if 'wk.dateTime' in request.POST:
		wkdateTime = request.POST['wk.dateTime']
	entities = dengon.objects.all()
	return render(request, 'list.html', {'entities':entities})
