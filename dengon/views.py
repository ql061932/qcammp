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
	return render(request, 'input.html')

def list(request):
	#from input
	if 'input' in request.POST:
		#check
		form = dengonForm(request.POST)
		if not form.is_valid():
			return render(request, 'input.html', {'error':1})
		#create
		if 'nameTo' in request.POST:
			dengon.objects.update_or_create(nameTo=request.POST['nameTo'],
											nameFrom=request.POST['nameFrom'],
											nameTakenBy=request.POST['nameTakenBy'],
											requirement=request.POST['requirement'],
											phoneNumber=request.POST['phoneNumber'],
											message=request.POST['message'])

	#from list
	if 'search' in request.POST:
		#search with query
		entities = dengon.objects.filter(nameTo=request.POST['wk.nameTo'])
	else:
		#search all
		entities = dengon.objects.all()

	return render(request, 'list.html', {'entities':entities})