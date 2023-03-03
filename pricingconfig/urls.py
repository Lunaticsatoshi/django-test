from django.urls import path
from .views import get_price

urlpatterns = [
    path('price/', get_price, name='current-price'),
]