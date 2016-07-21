from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "plates_site/index.html")

def search(request):
	return render(request, "plates_site/search.html")

def plate(request):
	# get parameters: license, location
	license = request.GET.get('license', '')
	location = request.GET.get('location', '')
	return render(request, "plates_site/plate.html", {
		"location": location,
		"license": license,
	})
