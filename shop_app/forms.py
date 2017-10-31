from django.forms import ModelForm

from .models import Comment, Animal, Feed, AnimalType


class CommentPostForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'mark']
        exclude = ['animal']


class AnimalPostForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['type', 'image', 'breed', 'description', 'price']


class FeedPostForm(ModelForm):
    class Meta:
        model = Feed
        fields = ['name', 'description', 'price', 'animals']


class AnimalTypeForm(ModelForm):
    class Meta:
        model = AnimalType
        fields = ['type']
