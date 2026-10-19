from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('new/', views.new_article, name="new_article"),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('edit_article/<int:id>', views.edit, name="edit_article"),
    path('delete_article/<int:id>', views.delete_article, name="delete_article"),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
]