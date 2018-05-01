from django.shortcuts import render
from . import cat_facts_api

# Create your views here.

def home_page(request):
    return render(request, 'cat/homepage.html')


def get_facts(request):
    number = request.GET.get('number', '1') # get number, or 1 if not present. TODO make sure it's a number
    facts = cat_facts_api.get_facts(number)
    return render(request, 'cat/facts.html', { 'facts': facts})
