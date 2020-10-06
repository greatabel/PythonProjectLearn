from django.http import HttpResponse
from django.shortcuts import render
import psycopg2

# conn = psycopg2.connect(database="TPCC", user="postgres", password="postgres", host="localhost", port="5432")
# print("Opened database successfully")

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {
        'test': 'test',

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'AppLine/index.html', context=context)