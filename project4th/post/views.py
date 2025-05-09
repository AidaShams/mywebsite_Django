from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import post
from django.urls import reverse_lazy
#from .forms import PostForm

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
    # form_class = PostForm
    # success_url = reverse_lazy('post_listview')
    # def form_valid(self, form):
    #     return super().form_valid(form)

class post_updateview(UpdateView):
    template_name = "post/post_updateview.html"
    model = post
    fields = ['title','description','price','seller']
    # form_class = PostForm
    # success_url = reverse_lazy('post_listview')

class post_deleteview(DeleteView):
    template_name = "post/post_deleteview.html"
    model = post
    success_url = reverse_lazy('post_listview')

class home_class(TemplateView):
    template_name = "home.html"

