from django.shortcuts import render
from django.http import HttpResponse
from . import location


def index(request):
	return render(request, "plates_site/index.html")


def search(request):
	return render(request, "plates_site/search.html")


def plate(request):
    # get parameters: license, location
    license = request.GET.get('license', '')
    place = request.GET.get('location', '')
    license = "".join([i.upper() for i in license if i.lower() in 'abcdefghijklmnopqrstuvwxyz1234567890'])

    # check location is valid
    found = False
    for loc in location.locations:
        if loc.location == place:
            found = True
            try:
                loc.check_license(license)
            except:
                return render(request, "plates_site/search.html", {
                    "err": True,
                    "msg": "License not valid: the license \""+license+"\" is not valid in "+place+"."
                })
            break

    if not found:
        return render(request, "plates_site/search.html", {
            "err": True,
            "msg": "Location not valid: the location \""+place+"\" was not found."
        })

    return render(request, "plates_site/plate.html", {
        "location": place,
        "license": license,
    })
