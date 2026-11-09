from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, ListView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm


# ========= Guest functions =========
class Home(ListView):
    model = Article
    template_name = 'Blogs/home.html'
    context_object_name = 'articles'
    
class ArticleDetail(View):
    def get(self, request, id):
        article = get_object_or_404(Article, pk=id)
        return render(self.request, 'Blogs/article_detail.html', context={'article':article})

# ======== Admin functions =========

class New_article(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'Blogs/new_article.html'
    success_url = reverse_lazy('admin_page')

class Admin_Page(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'Blogs/admin_page.html'
    context_object_name = 'articles'

class Edit(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'Blogs/new_article.html'
    success_url = reverse_lazy('admin_page')
    pk_url_kwarg = 'id'
    
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    pk_url_kwarg = 'id'  
    success_url = reverse_lazy('admin_page')
    http_method_names = ['post'] 

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')