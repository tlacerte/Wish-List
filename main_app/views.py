from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import WishList

def index(request): 
  wish_list = WishList.objects.all()
  return render(request, 'index.html', { 'wish_list': wish_list })

class CreateWish(CreateView):
  model = WishList
  fields = '__all__'
  success_url = '/'

class DeleteWish(DeleteView):
  model = WishList
  success_url = '/'