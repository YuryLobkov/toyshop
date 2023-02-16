from django.urls import path, include
from .views import ShowcaseMainView
from . import views

urlpatterns = [
    path('', ShowcaseMainView.as_view(), name='main_view'),
    path('<slug>', views.toy_detail, name='toy-detail'),
    path('purchase/<slug>', views.purchase, name='purchase'),
    path('order/', views.OrderPage.as_view(), name='order'),
    path('thank-you/<int:pk>', views.purchase_thank_you, name='thank-you'),
]