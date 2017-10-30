from django.forms import ModelForm

from .models import Comment


class CommentPostForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'mark']
        exclude = ['animal']

