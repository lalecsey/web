from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return HttpResponse('<h3>Наши контакты</h3>')

def hello(request):
    return HttpResponse('<h1>Hello, world!</h1>')