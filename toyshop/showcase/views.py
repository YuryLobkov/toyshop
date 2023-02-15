from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
"""
PROJECT IMPORTS
"""
from .models import Toy

# Create your views here.

class ShowcaseMainView(ListView):
    model = Toy
    template_name = "showcase/index.html"

def toy_detail(request, slug):
    toy = get_object_or_404(Toy, slug=slug)
    return render(request, 'showcase/toy_detail.html', {'toy':toy})



def purchase_page():
    pass


def order_page():
    pass