from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return render(request,'virat.html')

def abd(request):
    return HttpResponse('<h1><center>Mr 360 Player</center></h1>')