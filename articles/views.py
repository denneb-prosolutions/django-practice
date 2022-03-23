from django.shortcuts import render

# Create your views here.
def denneb_articles(request):
    return render(request, "articles/denneb_articles.html")

def home(request):
    return render(request, "articles/home.html")