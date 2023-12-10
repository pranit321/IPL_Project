from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rohit(request):
    return render(request,'rohit.html')

def polard(request):
    return HttpResponse('<h1><center>Underrated Player</center></h1>')