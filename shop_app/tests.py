from django.test import TestCase
from django.urls import reverse

from shop_app.forms import AnimalTypeForm
from .models import AnimalType, Animal


class AnimalTest(TestCase):
    def create_animal(self):
        type = AnimalType.objects.create(type='cat')
        return Animal.objects.create(type=type,
                                     breed='good cat',
                                     color='brown',
                                     description='good cat for good man',
                                     price=100)

    # model tests
    def test_animal_creation(self):
        animal = self.create_animal()
        self.assertTrue(isinstance(animal, Animal))
        self.assertEqual(animal.__str__(), animal.breed)

    def test_animal_cat_default_image(self):
        cat_animal = self.create_animal()
        self.assertEqual(cat_animal.image_url(), '/static/images/default_cat.jpg')

    # view test
    def test_animal_list_view(self):
        url = reverse('animal_list')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertQuerysetEqual(resp.context['animals'], [])


class AnimalTypeTest(TestCase):
    def create_type(self):
        return AnimalType.objects.create(type='cat')

    # model test
    def test_animal_type_creation(self):
        animal_type = self.create_type()
        self.assertTrue(isinstance(animal_type, AnimalType))
        self.assertEqual(animal_type.__str__(), animal_type.type)

    # form tests
    def test_animal_type_valid_form(self):
        animal_type = self.create_type()
        data = {'type': animal_type.type}
        form = AnimalTypeForm(data=data)
        self.assertTrue(form.is_valid())

    def test_animal_type_invalid_form(self):
        data = {'type': ''}
        form = AnimalTypeForm(data=data)
        self.assertFalse(form.is_valid())


