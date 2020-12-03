from django.db import models

# Модель категория вопроса (общая/оформление/программирование...) минимум 5
# Название, описание, связь один ко многим модель -> статья
# группировка по категорим


class Category(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    user_name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    text = models.TextField(verbose_name='Текст')
    date_send = models.DateField(auto_now=True)

    date_answer = models.DateField(blank=True, null=True)
    text_answer = models.TextField(verbose_name='Текст ответа')
    is_show = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title