from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index.html')

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})

def home(request):
    # Work of Socket IO.
    # Continued.
    if request.method == "POST":
	nick = request.POST.get('nick','')
	return render(request, 'home.html', {'nick':nick})
    else:
	return render(request, 'db.html')
