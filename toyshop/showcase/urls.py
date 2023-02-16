from django.urls import path, include
from .views import ShowcaseMainView
from . import views

urlpatterns = [
    path('', ShowcaseMainView.as_view(), name='main_view'),
    path('<slug>', views.toy_detail, name='toy-detail'),
    path('purchase/<slug>', views.purchase, name='purchase'),
    path('order/', views.OrderPage.as_view(), name='order'),
    path('thank-you/<int:pk>', views.purchase_thank_you, name='thank-you'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('thank_you_for_you_feedback/', views.contact_us_thank_you, name='feedback-thank-you')
]