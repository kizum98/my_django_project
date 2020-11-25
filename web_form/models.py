from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок статьи')
    user_name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    text = models.TextField(verbose_name='Текст')
    date_send = models.DateField(auto_now=True)

    text_answer = models.TextField(verbose_name='Текст ответа')

    def __str__(self):
        return self.title