from django.http import HttpResponse
from django.shortcuts import render

def button(request):
    return render (request,'home.html')

def output(request):
    print("hello")
    data="hello"
    return render(request,‘home.html‘,{‘data‘:data})

def index(request):
    return HttpResponse("Hello, world.")
