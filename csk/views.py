from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def msd(request):
    return render(request,'msd.html')

def raina(request):
    return HttpResponse('<h1><center>Mr Ipl</center></h1>')