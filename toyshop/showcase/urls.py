from django.urls import path, include
from .views import ShowcaseMainView

urlpatterns = [
    path('', ShowcaseMainView.as_view()),
]