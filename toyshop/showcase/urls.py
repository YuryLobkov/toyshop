from django.urls import path, include
from .views import ShowcaseMainView
from . import views

urlpatterns = [
    path('', ShowcaseMainView.as_view(), name='main_view'),
    path('<slug>', views.toy_detail, name='toy-detail'),
    path('purchase/<slug>', views.PurchasePage.as_view(), name='purchase'),
    path('order/', views.OrderPage.as_view(), name='order')
]