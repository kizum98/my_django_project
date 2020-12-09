from django import forms
from captcha.fields import CaptchaField

from .models import Article


class CreateArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робо ')

    class Meta:
        model = Article
        fields = ['title', 'user_name', 'text']

    def __init__(self, *args, **kwargs):
        super(CreateArticleForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class': 'form-control col-6 col-10-sm',
        #                                           'placeholder': 'Название статьи'})
        # self.fields['user_name'].widget.attrs.update({'class': 'form-control col-6',
        #                                               'placeholder': 'Имя пользователя'})
        # self.fields['text'].widget.attrs.update({'class': 'form-control col-6',
        #                                          'placeholder': 'Текст'})


class AnswerArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робо ')

    class Meta:
        model = Article
        fields = ['text_answer', 'is_show']

    def __init__(self, *args, **kwargs):
        super(AnswerArticleForm, self).__init__(*args, **kwargs)
        self.fields['is_show'].widget.attrs.update({'class': 'form-check-input', 'type': 'checkbox'})


class SearchForm(forms.Form):
    filt = forms.CharField(max_length=100, initial="", required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control mr-4',
                                                         'placeholder': 'Введите название статьи'}))
