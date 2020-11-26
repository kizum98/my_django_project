from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import date

from .forms import AnswerArticleForm, CreateArticleForm
from .models import Article


def get_article(article_id):
    try:
        return Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найденна!")


def list_articles_view(request):
    articles_qs = Article.objects.order_by('date_send').order_by('title')[:30]
    return render(request, 'web_form/articles_list.html', {'articles_qs': articles_qs})


def article_create(request):
    form = CreateArticleForm(request.POST or None)
    reset = False

    if request.method == "POST":
        if form.is_valid():
            article = form.save()
            form = AnswerArticleForm(request.POST or None, instance=article)
            return render(request, 'web_form/article.html', {'article': article, 'form': form})
        reset = True

    return render(request, 'web_form/article_crate.html', {'form': form, 'reset': reset})


def article_view(request, article_id):
    article = get_article(article_id)
    form = AnswerArticleForm(request.POST or None, instance=article)
    reset = False

    if request.method == "POST":
        if form.is_valid():
            article = form.save()
            article.date_answer = date.today()
            return render(request, 'web_form/article.html', {'article': article, 'form': form, 'reset': reset})
        reset = True

    return render(request, 'web_form/article.html', {'article': article, 'form': form, 'reset': reset})


def article_modify(request, article_id):
    article = get_article(article_id)
    form = CreateArticleForm(request.POST or None, instance=article)
    reset = False

    if request.method == "POST":
        if form.is_valid():
            article = form.save()
            form = AnswerArticleForm(request.POST or None, instance=article)
            return render(request, 'web_form/article.html', {'article': article, 'form': form, 'reset': reset})
        reset = True

    return render(request, 'web_form/article_crate.html', {'form': form, 'reset': reset})