from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Hello, world. You're at the vimss_app home.")

def simple_ms1(request):
    return HttpResponse("You're looking at: simple_ms1")

def dia(request):
    return HttpResponse("You're looking at: dia")

def multiple_sample(request):
    return HttpResponse("You're looking at: multiple_sample")

def top_n(request):
    return HttpResponse("You're looking at: top_n")