from pydoc import render_doc
import django

from django.http import HttpResponse
from django.shortcuts import render
 
def denneb(request):
    return render(request,'denneb.html')

def homepage(request):
    return render(request, "home.html")