from django import forms
from captcha.fields import CaptchaField

from .models import Article

class CreateArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робо ')

    class Meta:
        model = Article
        fields = ['title', 'user_name', 'text', 'file']

    def __init__(self, *args, **kwargs):
        super(CreateArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control',
                                                   'placeholder': 'Название статьи'})
        self.fields['user_name'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Имя пользователя'})
        self.fields['text'].widget.attrs.update({'class': 'form-control',
                                                'placeholder': 'Текст'})
        self.fields['file'].widget.attrs.update({'class': '',
                                                 'widget': ''})


class AnswerArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='Докажи что не робо ')

    class Meta:
        model = Article
        fields = ['text_answer', 'is_show']

    def __init__(self, *args, **kwargs):
        super(AnswerArticleForm, self).__init__(*args, **kwargs)
        self.fields['text_answer'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Текст'})


class SearchForm(forms.Form):
    filt = forms.CharField(max_length=100, initial="", required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control mr-4',
                                                         'placeholder': 'Введите название статьи'}))
