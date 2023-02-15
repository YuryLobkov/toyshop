from django.urls import path, include
from .views import ShowcaseMainView
from . import views

urlpatterns = [
    path('', ShowcaseMainView.as_view()),
    path('<slug>', views.toy_detail, name='toy-detail'),
    path('purchase/<slug>', views.purchase_page, name='purchase'),
    path('order/<slug>', views.order_page, name='order')
]