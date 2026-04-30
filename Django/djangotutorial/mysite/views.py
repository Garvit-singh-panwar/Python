from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello world you are at Django tutorial home page");
    return render(request , 'website/index.html')

def about(request):
    return HttpResponse("hello world you are at Django tutorial about page");

def contact(request):
    return HttpResponse("hello world you are at Django tutorial contact page");