from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse, reverse_lazy
"""
PROJECT IMPORTS
"""
from .models import Toy, Order, Feedback
from .forms import OrderForm, PurchaseForm, ContactUsForm

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
        return reverse('thank-you')#, kwargs={'order_id':self.object.id})
        # return reverse('thank-you', kwargs={'order_id':self.object.id})
    
# class OrderConfirmationPage(View):
#     template_name = 'showcase/thank_you.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["order_id"] = kwargs.object.id
#         return context
    


def order_confirmation_page(request):
    # order_id = request.POST.get('post-id')
    order_id = Order.objects.get_queryset().values('id').last()
    # order_id = 5
    return render(request, 'showcase/thank_you.html', {'order_id':order_id})


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
            return redirect(order.get_absolute_url())
            # return render(request, 'showcase/thank_you.html', {'order':order} )
    return render(request, 'showcase/purchase_page.html', {'form':form,
                                                           'purchased_toy':purchased_toy})


def purchase_thank_you(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'showcase/thank_you.html', {'order':order})


def contact_us(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            feedback = Feedback.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                subject = request.POST.get('subject'),
                message = request.POST.get('message')
            )
            feedback.save()
            return redirect('feedback-thank-you')
    return render(request, 'showcase/contact_us.html', {'form':form})

def contact_us_thank_you(request):
    return render(request, 'showcase/contact_us_thank_you.html')