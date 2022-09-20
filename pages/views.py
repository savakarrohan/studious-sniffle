from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    """First Home Page view"""
    return HttpResponse("Hello World!")