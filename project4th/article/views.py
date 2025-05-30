from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import UpdateView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

class article_list(ListView):
    template_name = "article/list.html"
    model = Article

class article_detail(DetailView):
    template_name = "article/detail.html"
    model = Article

class article_update(UpdateView):
    template_name = "article/update.html"
    model = Article
    success_url = reverse_lazy("list")
    fields = ['title','description']

class article_delete(DeleteView):
    template_name = "article/delete.html"
    model = Article
    success_url = reverse_lazy("list")

class article_create(CreateView):
    template_name = "article/create.html"
    model = Article
    success_url = reverse_lazy("list")
    fields = ['title','description']
    def form_valid(self, form):
        form.instance.author = self.request.user        #this is for author_id 
        return super().form_valid(form)