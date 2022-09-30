"""forms.py"""
from django import forms
from posts.models import POST_TYPE_CHOICE


class PostForms(forms.Form):
    title = forms.CharField(label='Имя Прилагательное', max_length=100, min_length=8)
    description = forms.CharField(
        widget=forms.Textarea(),
        label='Описание'
    )
    stars = forms.IntegerField(
        max_value=5,
        min_value=0,
        label='Звездочки'
    )
    type = forms.ChoiceField(
        choices=POST_TYPE_CHOICE,
        label='Тип'
    )


class CommentForms(forms.Form):
    author = forms.CharField(label='Автор', max_length=100, min_length=2)
    text = forms.CharField(
        widget=forms.Textarea(),
        label='ты знаешь что сюда писать'
    )
