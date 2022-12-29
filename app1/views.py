from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def string1 (request):
    return HttpResponse('<h1>savitha is a good gril</h1>')

def string2(request):
    return HttpResponse('<h1>madhura is a good gril</h1>')