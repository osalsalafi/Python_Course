import django
from django.shortcuts import render
# you have to call HTTPresponse class from django
from django.http import HttpResponse
# Create your views here.
def hello_world(request):
    # we can fatch data from database
    # we have to do url mapping to match between function and url >> so create url.py
    return HttpResponse("Hello world!")

def main_page(request2):
    main_page_tilte = 'This is the first webpage created by Eng. Osama'
    return HttpResponse(main_page_tilte)

def articles(request, id, slug) :
    return HttpResponse(f"Article {id} for {slug}")