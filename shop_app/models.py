from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.type


class Animal(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='image')
    breed = models.CharField(max_length=50)
    authors = models.ManyToManyField(Feed)
    description = models.TextField()

    def __str__(self):
        return self.breed

    def image_url(self):
        """
        Returns the URL of the image associated with this Object.
        If an image hasn't been uploaded yet, it returns a stock image
        :returns: str -- the image url

        """
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/images/default_animal.png'


class Feed(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment_title = models.CharField(max_length=50)
    comment_auth = models.CharField(max_length=50, default='Anonim')
    comment_text = models.TextField()
    book = models.ForeignKey(Animal, on_delete=models.CASCADE)
    mark = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.comment_title
