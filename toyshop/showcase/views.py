from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse
"""
PROJECT IMPORTS
"""
from .models import Toy, Order
from .forms import OrderForm, PurchaseForm

# Create your views here.

class ShowcaseMainView(ListView):
    model = Toy
    template_name = "showcase/index.html"


def toy_detail(request, slug):
    toy = get_object_or_404(Toy, slug=slug)
    return render(request, 'showcase/toy_detail.html', {'toy':toy, 'self_slug': slug})


class PurchasePage(CreateView):
    template_name = 'showcase/purchase_page.html'
    form_class = PurchaseForm
    model = Order
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['purchasing_toy'] = Toy.objects.filter(slug = slug).all
        return context
    
    # Adding reference to purchasable toy in order table
    def form_valid(self, form):
        form.instance.purchase_exist = Toy.objects.filter(slug = self.kwargs['slug'])[0]
        form.save()
        return super().form_valid(form)
    

# TODO send emails
# TODO reverse url to thank u page
    def get_success_url(self):
        return reverse('main_view')


class OrderPage(CreateView):
    template_name = 'showcase/order_page.html'
    form_class = OrderForm
    model = Order

    def get_success_url(self):
        return reverse('main_view')
