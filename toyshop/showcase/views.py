from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
"""
PROJECT IMPORTS
"""
from .models import Toy
from .forms import OrderForm, PurchaseForm

# Create your views here.

class ShowcaseMainView(ListView):
    model = Toy
    template_name = "showcase/index.html"


def toy_detail(request, slug):
    toy = get_object_or_404(Toy, slug=slug)
    return render(request, 'showcase/toy_detail.html', {'toy':toy})


def purchase_page(request):
    form = PurchaseForm()
    return render(request, 'showcase/purchase_page.html', {'form':form})


def order_page(request):
    form = OrderForm()
    return render(request, 'showcase/order_page.html', {'form':form})