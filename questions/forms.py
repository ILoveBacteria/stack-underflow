from django import forms

from .models import Question, Answer, Tag


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'tags']


class AnswerForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Answer
        fields = ['body']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=255)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
