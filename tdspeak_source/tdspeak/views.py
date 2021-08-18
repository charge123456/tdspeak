from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse('Welcome SYWUSpeak System!')
    return render(request, 'index/index.html')
