from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView, View
from django.urls import reverse, reverse_lazy
import asyncio
from asgiref.sync import sync_to_async

"""
PROJECT IMPORTS
"""
from .models import Toy, Order
from .forms import OrderForm, PurchaseForm
from .email_sender import email_customer_order, email_admin_notification

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
        email_admin_notification(self.request, self.object.customer_name, self.object)
        return reverse('thank-you', kwargs={'pk':self.object.id})


#===============================================================

async def purchase(request, slug):
    purchased_toy = await sync_to_async(get_object_or_404)(Toy, slug=slug)
    form = PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            order = await sync_to_async(Order.objects.create)(
                email = request.POST.get('email'),
                customer_name = request.POST.get('customer_name'),
                phone_number = request.POST.get('phone_number'),
                preferable_messenger = request.POST.get('preferable_messenger'),
                comment = request.POST.get('comment'),
                purchase_exist = purchased_toy
            )
            await sync_to_async(order.save)()
            task1 = asyncio.ensure_future(email_customer_order(request, order.customer_name, order.email, order))
            task2 = asyncio.ensure_future(email_admin_notification(request, order.customer_name, order))
            await asyncio.wait([task1, task2])
            return redirect(order.get_absolute_url())
            # return render(request, 'showcase/thank_you.html', {'order':order} )
    return await sync_to_async(render)(request, 'showcase/purchase_page.html', {'form':form,
                                                           'purchased_toy':purchased_toy})


def purchase_thank_you(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'showcase/thank_you.html', {'order':order})