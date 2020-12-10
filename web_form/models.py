from django.db import models
import os
import uuid
import time


# Модель категория вопроса (общая/оформление/программирование...) минимум 5
# Название, описание, связь один ко многим модель -> статья
# группировка по категорим


class Category(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return self.title


def get_path(instance, filename):
    path = f'web_form/article/{time.strftime("%Y/%m/%d")}'
    ext = filename.split('.')[-1]
    fileid = f"{uuid.uuid4()}.{ext.lower()}"
    return os.path.join(path, fileid)


class Article(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Заголовок статьи')
    user_name = models.CharField(max_length=30,
                                 verbose_name='Имя пользователя')
    text = models.TextField(verbose_name='Текст')
    date_send = models.DateField(auto_now=True)
    file = models.ImageField(null=True, blank=True,
                             upload_to=get_path,
                             verbose_name='Загрузите файл')

    date_answer = models.DateField(blank=True, null=True)
    text_answer = models.TextField(verbose_name='Текст ответа')
    is_show = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_img(self):
        return "web_form/" + self.file.upload_to
