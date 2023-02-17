from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView, View
from django.urls import reverse, reverse_lazy
"""
PROJECT IMPORTS
"""
from .models import Toy, Order
from .forms import OrderForm, PurchaseForm
from .email_sender import email_customer_order

# Create your views here.

class ShowcaseMainView(ListView):
    model = Toy
    template_name = "showcase/index.html"


def toy_detail(request, slug):
    toy = get_object_or_404(Toy, slug=slug)
    return render(request, 'showcase/toy_detail.html', {'toy':toy, 'self_slug': slug})

# TODO send emails
# TODO reverse url to thank u page


class OrderPage(CreateView):
    template_name = 'showcase/order_page.html'
    form_class = OrderForm
    model = Order

    def get_success_url(self):
        email_customer_order(self.request, self.object.customer_name, self.object.email, self.object)
        return reverse('thank-you', kwargs={'pk':self.object.id})


#===============================================================

def purchase(request, slug):
    purchased_toy = get_object_or_404(Toy, slug=slug)
    form = PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                email = request.POST.get('email'),
                customer_name = request.POST.get('customer_name'),
                phone_number = request.POST.get('phone_number'),
                preferable_messenger = request.POST.get('preferable_messenger'),
                comment = request.POST.get('comment'),
                purchase_exist = purchased_toy
            )
            order.save()
            email_customer_order(request, order.customer_name, order.email, order)
            return redirect(order.get_absolute_url())
            # return render(request, 'showcase/thank_you.html', {'order':order} )
    return render(request, 'showcase/purchase_page.html', {'form':form,
                                                           'purchased_toy':purchased_toy})


def purchase_thank_you(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'showcase/thank_you.html', {'order':order})