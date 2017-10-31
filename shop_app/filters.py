import django_filters
from django import forms
from .models import Animal, Feed


class AnimalFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt')


    class Meta:
        model = Animal
        fields = ['type']
