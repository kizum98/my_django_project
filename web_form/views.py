from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import date, timedelta
from django.db.models import Count, Q

from .forms import AnswerArticleForm, CreateArticleForm
from .models import Article

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class MyPaginator:
    def __init__(self, qs, num_elements_on_page=1):
        self.qs = qs
        self.num_elements_on_page = num_elements_on_page
        self.num_pages = len(qs) / num_elements_on_page

    def page(self, num_page):

        if num_page is int and 0 < num_page < self.num_pages + 1:
            start = self.num_elements_on_page * (num_page - 1)
            end = self.num_elements_on_page * num_page
        else:
            start = 0
            end = self.num_elements_on_page
            num_page = 1

        p = self.Page(self.qs[start:end], num_page)
        if start == 0:
            p.has_previous = False
        if end == self.num_elements_on_page * num_page:
            p.has_next = False

        return p

    class Page:
        has_previous = True
        has_next = True

        def __init__(self, qs, next_page_number):
            self.qs = qs
            self.it = 0
            self.next_page_number = next_page_number
            print(self.next_page_number)

        def __iter__(self):
            return self

        def __next__(self):
            if self.it < len(self.qs):
                val = self.qs[self.it]
                self.it += 1
                return val
            else:
                raise StopIteration


def get_article(article_id):
    try:
        return Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найденна!")


def list_articles_view(request):
    # Найти все записи за последнюю неделю
    # articles_qs = Article.objects.filter(date_send__gt=date.today() - timedelta(days=7)).order_by('-date_send')
    #
    # Найти записи, где в вопросе, ответе и имени пользователя есть слово "Привет", с учетом регистра
    # articles_qs = Article.objects.filter(user_name__contains="Привет", text__contains="Привет",
    #                                      text_answer__contains="Привет").order_by('-date_send')
    #
    # Найти записи, где в вопросе, ответе и имени пользователя есть слово "Привет", без учета регистра
    # articles_qs = Article.objects.filter(user_name__iregex=r'Привет', text__iregex=r'Привет',
    #                                      text_answer__iregex=r'Привет')).order_by('-date_send')
    #
    # Сколько записей is_show=True
    # num_articles = Article.objects.filter(is_show=True).count()
    # print(num_articles)
    #
    # Сколько записей s_show=False
    # num_articles = Article.objects.filter(is_show=False).count()
    # print(num_articles)
    #
    # Сколько запросов послал каждый из пользователей
    # num_user_articles_list = Article.objects.values('user_name').annotate(Count('user_name'))
    # for i in range(0, len(num_user_articles_list)):
    #    print(num_user_articles_list[i]['user_name'], num_user_articles_list[i]['user_name__count'])
    #
    # Найти записи, где в вопросе или ответе или имени пользователя есть слово "Привет", с учетом регистра
    # articles_qs = Article.objects.filter(Q(user_name__contains="Привет") | Q(text__contains="Привет") |
    #                                      Q(text_answer__contains="Привет")).order_by('-date_send')
    #
    #
    # Найти записи, где в вопросе или ответе или имени пользователя есть слово "Привет", без учета регистра
    # articles_qs = Article.objects.filter(Q(user_name__iregex=r'Привет') | Q(text__iregex=r'Привет') |
    #                                      Q(text_answer__iregex=r'Привет')).order_by('-date_send')

    # articles_qs = Article.objects.order_by('-date_send', 'title')[:10]
    # return render(request, 'web_form/articles_list.html', {'articles_qs': articles_qs})

    articles_qs = Article.objects.order_by('-date_send', 'title')
    paginator = MyPaginator(articles_qs, 10)
    num_page = request.GET.get('page')
    page = paginator.page(num_page)
    # try:
    #     page = paginator.page(num_page)
    # except PageNotAnInteger:
    #     page = paginator.page(1)
    # except EmptyPage:
    #     page = paginator.page(paginator.num_pages)

    return render(request, 'web_form/articles_list.html', {'page': page})


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
