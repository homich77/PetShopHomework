from django.db.models import Avg
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import ListView, DetailView, FormView

from shop_app.forms import CommentPostForm
from shop_app.models import Animal, Type


class AnimalList(ListView):
    template_name = 'shop_app/animal_list.html'
    model = Animal
    context_object_name = 'animal_list'

    def get_context_data(self, **kwargs):
        context = super(AnimalList, self).get_context_data(**kwargs)
        # sort animals by rank
        context['animals'] = Animal.objects.all().annotate(rank=Avg('comment__mark')).order_by('-rank')
        return context


class CommentAddView(FormView):
    template_name = 'shop_app/add_comment.html'
    form_class = CommentPostForm
    success_url = '/shop/'

    def post(self, request, pk):
        animal = Animal.objects.get(pk=pk)
        form = CommentPostForm(request.POST,
                               request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.animal = animal
            form.save()
            return HttpResponseRedirect('/shop/')
        return HttpResponse("Done")

    def get(self, request, pk):
        template = get_template('shop_app/add_comment.html')
        context = {
            'animal': Animal.objects.get(pk=self.kwargs.get('pk')),
            'form': CommentPostForm()
        }
        return HttpResponse(template.render(context, request))


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


def search_form(request):
    return render(request, 'shop_app/search_form.html')


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        animals = Animal.objects.filter(breed__icontains=q)
        return render(request, 'shop_app/animal_list.html',
                      {'animals': animals})

    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
