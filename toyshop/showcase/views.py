from django.shortcuts import render
from django.views.generic import ListView
"""
PROJECT IMPORTS
"""
from .models import Toy

# Create your views here.

class ShowcaseMainView(ListView):
    model = Toy
    template_name = "showcase/index.html"


def purchase_page():
    pass


def order_page():
    pass