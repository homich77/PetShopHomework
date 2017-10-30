from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Animal(models.Model):
    type = models.ForeignKey("AnimalType", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='image')
    breed = models.CharField(max_length=50)
    feed = models.ManyToManyField("Feed")
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)

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
            if str(self.type) == 'dog':
                return '/static/images/default_dog.jpg'
            if str(self.type) == 'cat':
                return '/static/images/default_cat.jpg'
            if str(self.type) == 'bird':
                return '/static/images/default_bird.jpg'
            else:
                return '/static/images/default_animals.jpg'


class Feed(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment_title = models.CharField(max_length=50)
    comment_auth = models.CharField(max_length=50, default='Anonim')
    comment_text = models.TextField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    mark = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.comment_title


class AnimalType(models.Model):
    ANIMALS_TYPES = (
        ('dog', 'dog'),
        ('cat', 'cat'),
        ('bird', 'bird'),
    )
    type = models.CharField(max_length=10, choices=ANIMALS_TYPES, default='dog')

    def __str__(self):
        return self.type
