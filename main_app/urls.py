from django.urls import path
from .views import index, CreateWish, delete

urlpatterns = [
  path('', index),
  path('add/', CreateWish.as_view(), name='add_wish'),
  path('delete/<int:id>', delete, name='delete_wish')
]