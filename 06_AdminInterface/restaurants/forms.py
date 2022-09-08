from django import forms
from .models import News, Comments


class NewsForm(forms.ModelForm):
    model = News

    class Meta:
        fields = "__all__"


class CommentsForm(forms.Form):
    model = Comments
    name = forms.CharField(label="Имя ")
    text = forms.CharField(label="Текст коментари ")
