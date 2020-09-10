from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'vimss_app/home.html')


def simple_ms1(request):
    return render(request, 'vimss_app/simple_ms1.html')


def dia(request):
    return render(request, 'vimss_app/dia.html')


def multiple_sample(request):
    return render(request, 'vimss_app/multiple_sample.html')


def top_n(request):
    return render(request, 'vimss_app/top_n.html')
