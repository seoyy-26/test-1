from django.http import request
from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def index(request):
    return render(request, 'main/index.html')

def left_sidebar(request):
    return render(request, 'main/left_sidebar.html')

def no_sidebar(request):
    return render(request, 'main/no_sidebar.html')

def right_sidebar(request):
    return render(request, 'main/right_sidebar.html')
