from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from .models import Article
from .forms import ArticleForm

# ========= Guest functions =========
def home(request):
    articles = Article.objects.all()
    return render(request, 'Blogs/home.html', context={'articles': articles})

def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'Blogs/article_detail.html', context={'article':article})

# ======== Admin functions =========
@login_required
def new_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = ArticleForm()
    return render(request, 'Blogs/new_article.html', context = {'form': form})

@login_required
def admin_page(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'Blogs/admin_page.html', context)

@login_required
def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'Blogs/new_article.html', context={'form': form})

@login_required
@require_POST
def delete_article(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    return redirect('admin_page')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})