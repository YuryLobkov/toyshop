from django.urls import path, include
from .views import ShowcaseMainView, homepage_view
from . import views

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('showcase/', ShowcaseMainView.as_view(), name='main_view'),
    path('purchase/<slug>', views.purchase, name='purchase'),
    path('order/', views.OrderPage.as_view(), name='order'),
    path('thank-you/<int:pk>', views.purchase_thank_you, name='thank-you'),
    path('order-table/', views.orders_table, name='order-table'),
    path('<slug>/', views.toy_detail, name='toy-detail'),
]