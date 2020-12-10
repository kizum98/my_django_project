from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.list_articles_view, name='list_articles_view'),
    path('article_create/', views.article_create, name='article_create'),
    path('<int:article_id>/', views.article_view, name='article_view'),
    path('<int:article_id>/modify/', views.article_modify, name='article_modify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
