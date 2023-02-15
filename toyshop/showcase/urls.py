from django.urls import path, include
from .views import ShowcaseMainView, toy_detail

urlpatterns = [
    path('', ShowcaseMainView.as_view()),
    path('<slug>', toy_detail, name='toy-detail'),
]