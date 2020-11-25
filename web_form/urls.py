from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.list_articles_view, name='list_articles_view'),
    path('article_create/', views.article_create, name='article_create'),
    path('<int:article_id>/', views.article_view, name='article_view'),
    path('modify_<int:article_id>/', views.article_modify, name='article_modify'),
]

