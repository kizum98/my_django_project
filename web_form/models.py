from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    user_name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    text = models.TextField(verbose_name='Текст')
    date_send = models.DateField(auto_now=True)

    date_answer = models.DateField(blank=True, null=True)
    text_answer = models.TextField(verbose_name='Текст ответа')
    is_show = models.BooleanField(default=False)

    def __str__(self):
        return self.title