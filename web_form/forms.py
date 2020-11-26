from django import forms
from captcha.fields import CaptchaField

from .models import Article


class CreateArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робо ')

    class Meta:
        model = Article
        exclude = ['date_send', 'text_answer']


class AnswerArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робо ')

    class Meta:
        model = Article
        fields = ['text_answer']