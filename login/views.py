from django.urls import path
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("<h1>hello world</h1>")