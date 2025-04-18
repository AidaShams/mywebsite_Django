from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import post
# Create your views here.
class post_listview(ListView):
    template_name = "post/post_listview.html"
    model = post
    context_object_name = "datas"

class post_detailview(DetailView):
    template_name = "post/post_detailview.html"
    model = post
    context_object_name = "datas"

class post_createview(CreateView):
    template_name = "post/post_createview.html"
    model = post
    fields = ['title','description', 'price', 'seller']