from django.db.models import Avg
from django.views.generic import ListView, DetailView

from shop_app.models import Animal, Type


class AnimalList(ListView):
    template_name = 'shop_app/animal_list.html'
    model = Animal
    context_object_name = 'animal_list'

    def get_context_data(self, **kwargs):
        context = super(AnimalList, self).get_context_data(**kwargs)
        context['animals'] = Animal.objects.all().annotate(rank=Avg('comment__mark')).order_by('-rank')
        return context


class AnimalDetails(DetailView):
    template_name = 'shop_app/animal_detail.html'
    context_object_name = 'animal'
    model = Animal


class TypeList(ListView):
    template_name = 'shop_app/types_list.html'
    model = Type
    context_object_name = 'types_list'

    def get_context_data(self, **kwargs):
        context = super(TypeList, self).get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class TypeDetail(DetailView):
    template_name = 'shop_app/type_detail.html'
    model = Type
    context_object_name = 'type'
