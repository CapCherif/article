

from django.shortcuts import render

from my_article.models import Article


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

def Add(request):
    added = False
    #si la fonction reçois des données
    # elle les enregistre dans la bd
    if request.method == "POST":
        title = request.POST['title']
        date = str(request.POST['date'])
        author = request.POST['author']
        description = request.POST['description']
        # save to db
        art = Article() # créer un objet de type Article
        art.title = title
        art.author = author
        art.date = date
        art.description = description
        art.save()
        added = True
    return render(request, "add.html", {"added":added})

# def addArticle(request):
#     # enregistrer les données reçus dans la base de données
