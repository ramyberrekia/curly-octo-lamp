from django.shortcuts import render, reverse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post 
from random import random
from taggit.models import Tag
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostCreateForm
from django.contrib import messages


class PostListView(ListView):
    model = Post 
    context_object_name = 'posts'
    paginate_by = 8
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Post.objects.recent_posts(self.get_object())
        return context
    

class PostTagList(ListView):
    model = Post 
    context_object_name = 'posts'
    paginate_by = 8
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super(PostTagList, self).get_queryset()
        queryset = Post.objects.tag_posts(tag=self.kwargs['slug'])
        return queryset


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse('blog:posts_list')

    def form_valid(self, form):
        form = form.save(commit=False)
        form.author = self.request.user
        form.save()
        messages.success(self.request, 'Your post has been created succesfully!')
        # get_success_url(slug=form.instance.slug)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Your post\'s creation failed.')
        return super(PostCreateView, self).form_invalid(form)
        


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostCreateForm

    def test_func(self):
        if self.request.user != self.get_object().author:
            return False
        else: 
            return True

    def get_success_url(self):
        return reverse('blog:posts_list')

    def form_valid(self, form):
        messages.success(self.request, 'Your post has been updated succesfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Your post\'s edit failed.')
        return super().form_invalid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        if self.request.user != self.get_object().author:
            return False
        else: 
            return True

    def get_success_url(self):
        return reverse('blog:posts_list')
