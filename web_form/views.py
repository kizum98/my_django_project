from django.shortcuts import render
from django.http import HttpResponse, Http404

from .forms import AnswerArticleForm, CreateArticleForm
from .models import Article


def list_articles_view(request):
    articles_qs = Article.objects.all()
    return render(request, 'web_form/articles_list.html', {'articles_qs': articles_qs})


def article_create(request):
    form = CreateArticleForm(request.POST or None)
    reset = False

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse(f"Сообщение {form['user_name'].value()} отправленно!")
        reset = True

    return render(request, 'web_form/article_crate.html', {'form': form, 'reset': reset})


def article_view(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найденна!")
    form = AnswerArticleForm(request.POST or None, instance=article)

    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse(f"Сообщение {form.is_valid(), form['text_answer'].value} отправленно!")

    return render(request, 'web_form/article.html', {'article': article, 'form': form})

def article_modify(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найденна!")
    form = CreateArticleForm(request.POST or None, instance=article)

    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse(f"Сообщение {form['user_name'].value()} измененно!")

    return render(request, 'web_form/article_crate.html', {'form': form})