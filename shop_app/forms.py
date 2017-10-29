from django.forms import ModelForm, Form, ChoiceField
from django import forms
from .models import Comment, Type


class CommentPostForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'mark']
        exclude = ['animal']


class AnimalSearch(Form):
    type = forms.ChoiceField(choices=Type.objects.all())