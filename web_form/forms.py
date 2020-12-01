from django import forms
from captcha.fields import CaptchaField

from .models import Article


class CreateArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робо ')

    class Meta:
        model = Article
        fields = ['title', 'user_name', 'text']


class AnswerArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робо ')

    class Meta:
        model = Article
        fields = ['text_answer', 'is_show']


class SearchForm(forms.Form):

    cond = forms.CharField(max_length=100, initial="", required=False)
