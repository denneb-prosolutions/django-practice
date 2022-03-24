from django.shortcuts import render
from .models import Articles
from .models import Books

# Create your views here.
def denneb_articles(request):
    books = Books.objects.all().order_by('datetime')
    return render(request, "articles/denneb_articles.html" , {"books": books})

def home(request):
    return render(request, "articles/home.html")