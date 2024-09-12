

from django.shortcuts import render


def Accueil(request):

    return render(request, "accueil.html", 
                  {"name":"Cherif", "age":31, "data":["Cherif", "Seddik", "Seif", "Lilia"]})

def Contact(request):
    #traitement
    #traitement

    return render(request, "contact.html")

def About(request):
    return render(request, "about.html")

def Service(request):
    return render(request, "service.html", {"name":"Cherif"})

