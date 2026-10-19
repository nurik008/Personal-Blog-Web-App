from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'published_at']  
        
        labels = {
            'title': 'Заголовок статьи',
            'content': 'Текст публикации',
            'published_at': 'Дата публикации',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Введите яркий заголовок...',
                'maxlength': '200',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Напишите здесь вашу статью...',
                'rows': 6,  
            }),
            'published_at': forms.DateInput(attrs={
                'type': 'date',  
            }),
        }