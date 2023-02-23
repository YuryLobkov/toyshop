from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, CreateView, View
from django.urls import reverse, reverse_lazy
import asyncio
import time
from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required

"""
PROJECT IMPORTS
"""
from .models import Toy, Order, Feedback
from .forms import OrderForm, PurchaseForm, ContactUsForm, FilterShowcaseForm
from .email_sender import email_customer_order, email_admin_notification

# Create your views here.


def homepage_view(request):
    return render(request, 'showcase/index.html')


class ShowcaseMainView(ListView):
    model = Toy
    template_name = "showcase/showcase.html"

    # TODO refactor it to DRY
    def get_queryset(self):
        all_toys = Toy.objects.all()
        if self.request.GET.get('material'):
            filter_material = self.request.GET.get('material', all_toys.values_list('material'))
        else:
            filter_material = all_toys.values_list('material')
        if self.request.GET.get('size'):
            filter_size = self.request.GET.get('size', all_toys.values_list('size'))
        else:
            filter_size = all_toys.values_list('size')
        if self.request.GET.get('category'):
            filter_category = self.request.GET.get('category', all_toys.values_list('category'))
        else:
            filter_category = all_toys.values_list('category')
        filter_in_stock_only = self.request.GET.get('in_stock', False)
        new_context = Toy.objects.filter(
            material__in=filter_material,
            size__in=filter_size,
            category__in=filter_category,
        )
        if filter_in_stock_only:
            return new_context.filter(in_stock = True)
        else:
            return new_context

    def get_context_data(self, **kwargs):
        context = super(ShowcaseMainView, self).get_context_data(**kwargs)
        filter_current_values = [0, 0, 0, False]
        if self.request.GET.get:
            filter_current_values = [
                self.request.GET.get('material'),
                self.request.GET.get('size'),
                self.request.GET.get('category'),
                self.request.GET.get('in_stock')
            ]
        context['filter_form'] = FilterShowcaseForm(initials=filter_current_values)
        # context['material'] = self.request.GET.get('material')
        return context


def toy_detail(request, slug):
    toy = get_object_or_404(Toy, slug=slug)
    return render(request, 'showcase/toy_detail.html', {'toy': toy, 'self_slug': slug})


class OrderPage(CreateView):
    template_name = 'showcase/order_page.html'
    form_class = OrderForm
    model = Order

# add order type
    def form_valid(self, form):
        order = form.save(commit=False)
        order.order_type = 'New toy order'
        order.save()
        return super(OrderPage, self).form_valid(form)

    def get_success_url(self):
        email_customer_order(
            self.request, self.object.customer_name, self.object.email, self.object)
        email_admin_notification(
            self.request, self.object.customer_name, self.object)
        return reverse('thank-you', kwargs={'pk': self.object.id})


# ===============================================================


"""

# ASYNC version of func
# async def purchase(request, slug):
#     purchased_toy = await sync_to_async(get_object_or_404)(Toy, slug=slug)
#     form = PurchaseForm()
#     if request.method == 'POST':
#         form = PurchaseForm(request.POST)
#         if form.is_valid():
#             order = await sync_to_async(Order.objects.create)(
#                 email = request.POST.get('email'),
#                 customer_name = request.POST.get('customer_name'),
#                 phone_number = request.POST.get('phone_number'),
#                 preferable_messenger = request.POST.get('preferable_messenger'),
#                 comment = request.POST.get('comment'),
#                 purchase_exist = purchased_toy
#             )
#             if purchased_toy:
#                 order.order_type = 'Toy from shop'
#             else:
#                 order.order_type = 'New toy order'
#             await sync_to_async(order.save)()
#             start_time = time.time()
#             task1 = asyncio.ensure_future(email_customer_order(request, order.customer_name, order.email, order))
#             task2 = asyncio.ensure_future(email_admin_notification(request, order.customer_name, order))
#             await asyncio.wait([task1, task2])
#             print('delay due to mail sending: ', time.time()-start_time) # 9,79 seconds
#             return redirect(order.get_absolute_url())
#     return await sync_to_async(render)(request, 'showcase/purchase_page.html', {'form':form,
#                                                            'purchased_toy':purchased_toy})

"""

# SYNC vertion of func


def purchase(request, slug):
    purchased_toy = get_object_or_404(Toy, slug=slug)
    form = PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                email=request.POST.get('email'),
                customer_name=request.POST.get('customer_name'),
                phone_number=request.POST.get('phone_number'),
                preferable_messenger=request.POST.get('preferable_messenger'),
                comment=request.POST.get('comment'),
                purchase_exist=purchased_toy
            )
            if purchased_toy:
                order.order_type = 'Toy from shop'
            else:
                order.order_type = 'New toy order'
            order.save()

            purchased_toy.quantity = purchased_toy.quantity-1
            if purchased_toy.quantity == 0:
                purchased_toy.in_stock = False
            purchased_toy.save()

            start_time = time.time()
            email_customer_order(
                request, order.customer_name, order.email, order)
            email_admin_notification(request, order.customer_name, order)
            print('delay due to mail sending: ',
                  time.time()-start_time)  # 9,79 seconds
            return redirect(order.get_absolute_url())
    return render(request, 'showcase/purchase_page.html', {'form': form,
                                                           'purchased_toy': purchased_toy})


def purchase_thank_you(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'showcase/thank_you.html', {'order': order})


@login_required
def orders_table(request):
    orders = Order.objects.filter(closed=False)
    if request.method == 'POST':
        order = get_object_or_404(Order, id=request.POST.get('id'))
        order.closed = bool(request.POST.get('closed'))
        order.save()
        return redirect(reverse('order-table'))

    return render(request, 'showcase/orders_table.html', {'orders': orders})



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