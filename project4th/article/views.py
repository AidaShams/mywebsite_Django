from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import UpdateView, FormMixin

from .forms import CommentForm
from .models import Article
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
# Create your views here.

class article_list(ListView):
    template_name = "article/list.html"
    model = Article

class article_detail(FormMixin,DetailView):
    template_name = "article/detail.html"
    model = Article
    form_class = CommentForm
    def get_success_url(self):
        return reverse('detail',self, kwargs={'pk': self.object.pk})
    def get_context_data(self, **kwargs):
        form = super(article_detail,self).get_context_data(**kwargs)
        form['form']=CommentForm(initial={'comment':self.object, 'writer':self.request.user})
        return form
    def post(self, *args, **kwargs):
        self.object=self.get_object()
        form=self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            pass
    def form_valid(self, form):
        form.save()
        return super(article_delete, self).form_valid(form)

class article_update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = "article/update.html"
    model = Article
    success_url = reverse_lazy("list")
    fields = ['title','description','author']
    def test_func(self):
        obj = self.get_object()                     #this is for testing to make sure the right author can make changes
                                                    # to the article they wrote
        return obj.author == self.request.user

    # def test_func(self):
    #     # Example: Only allow access if the user is a superuser
    #     return self.request.user.is_superuser


class article_delete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    template_name = "article/delete.html"
    model = Article
    success_url = reverse_lazy("list")
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class article_create(LoginRequiredMixin,CreateView):
    template_name = "article/create.html"
    model = Article
    success_url = reverse_lazy("list")
    fields = ['title','description']
    def form_valid(self, form):
        form.instance.author = self.request.user        #this is for author_id 
        return super().form_valid(form)