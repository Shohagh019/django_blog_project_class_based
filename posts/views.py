from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

method_decorator(login_required, name= 'dispatch')
class CreatePost(CreateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user 
        # because when i add post i dont need to see ar add my own name.it will do automatically
        return super().form_valid(form)
         
method_decorator(login_required, name= 'dispatch')
class EditPost(UpdateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'post.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

method_decorator(login_required, name= 'dispatch')
class DeletePost(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'