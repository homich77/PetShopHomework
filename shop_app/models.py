from django.db import models
from django.urls import reverse


class Feed(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    animals = models.ManyToManyField("Animal")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('feed_detail', kwargs={'pk': self.id})


class Animal(models.Model):
    type = models.ForeignKey("AnimalType", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='animals_img')
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50, default="black")
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

    def get_absolute_url(self):
        return reverse('animal_detail', kwargs={'pk': self.id})


class Comment(models.Model):
    comment_title = models.CharField(max_length=50)
    comment_auth = models.CharField(max_length=50, default='Anonim')
    comment_text = models.TextField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], default=1
    )

    def __str__(self):
        return self.comment_title


class AnimalType(models.Model):
    type = models.CharField(max_length=10, default='dog')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('type_detail', kwargs={'pk': self.id})


class Cart(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    animals = models.ManyToManyField(Animal, through='OrderAnimal')

    OPEN = 'open'
    CLOSED = 'closed'
    ORDER_STATUS = ((OPEN, 'open'), (CLOSED, 'closed'))
    status = models.CharField(max_length=20, choices=ORDER_STATUS)

    def __str__(self):
        return self.status


class OrderAnimal(models.Model):
    order = models.ForeignKey(Cart, related_name='order_animals', on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal)
    quantity = models.PositiveIntegerField()

    def _get_total(self):
        return self.animal.price * self.quantity

    total_sum = property(_get_total)
