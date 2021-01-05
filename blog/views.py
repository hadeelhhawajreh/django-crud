from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from .models import ModelBlog

from django.urls import reverse_lazy
# Create your views here.

class HomeBlogView(ListView):
    template_name='home.html'
    model=ModelBlog


class DetailsBlogView(DetailView):
    template_name='details.html'
    model=ModelBlog

class BlogCreate(CreateView):
    template_name='create_blog.html'
    model=ModelBlog
    fields=['title','author','body']

class BlogUpdate(UpdateView):
    template_name='update_blog.html'
    model=ModelBlog
    fields=['title','author','body']


class BlogDelete(DeleteView):
    template_name='delete_blog.html'
    model=ModelBlog
    fields=['title','author','body']
    success_url=reverse_lazy('home')

    


