from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "plates_site/index.html")

def search(request):
	return render(request, "plates_site/search.html")
