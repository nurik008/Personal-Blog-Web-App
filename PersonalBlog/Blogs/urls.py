from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('article/<int:id>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('new/', views.New_article.as_view(), name="new_article"),
    path('admin_page/', views.Admin_Page.as_view(), name='admin_page'),
    path('edit_article/<int:id>', views.Edit.as_view(), name="edit_article"),
    path('delete_article/<int:id>', views.ArticleDeleteView.as_view(), name="delete_article"),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    
    path('api/articles/', views.HomeApiView.as_view(), name='api_articles'),
    path('api/articles/<int:id>/', views.ArticleDetailApiView.as_view(), name='api_article_detail'),
    path('api/articles/create/', views.ArticleCreateApiView.as_view(), name='api_article_create'),
    path('api/articles/<int:id>/update/', views.ArticleUpdateApiView.as_view(), name='api_article_update'),
    path('api/articles/<int:id>/delete/', views.ArticleDeleteApiView.as_view(), name='api_article_delete'),
]