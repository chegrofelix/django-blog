from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(respose):
    return HttpResponse('<h1>blog-home</h1>')

def about(respose):
    return HttpResponse('<h1>blog-about</h1>')