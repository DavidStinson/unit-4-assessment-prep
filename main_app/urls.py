from django.urls import path
from .views import index, CreateWish

urlpatterns = [
  path('', index),
  path('add/', CreateWish.as_view(), name='add_wish'),
]