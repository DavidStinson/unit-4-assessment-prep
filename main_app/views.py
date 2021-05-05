from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Wishlist

# Create your views here.

def index(request):
  wishlist = Wishlist.objects.all()
  return render(request, 'index.html', {'wishlist': wishlist})

class CreateWish(CreateView):
  model = Wishlist
  fields = '__all__'
  template_name = 'add.html'
  success_url = '/'

def delete(request, id):
  Wishlist.objects.get(id=id).delete()
  return redirect('/')