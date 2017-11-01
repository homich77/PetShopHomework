import django_filters

from .models import Animal


class AnimalFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt')

    class Meta:
        model = Animal
        fields = ['type']
