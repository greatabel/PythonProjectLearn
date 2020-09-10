from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'vimss_app/home.html')


def simple_ms1(request):
    return HttpResponse("You're looking at: simple_ms1")


def dia(request):
    return HttpResponse("You're looking at: dia")


def multiple_sample(request):
    return HttpResponse("You're looking at: multiple_sample")


def top_n(request):
    return HttpResponse("You're looking at: top_n")
