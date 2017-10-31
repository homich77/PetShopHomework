from django.db.models import Avg
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView

from shop_app.forms import CommentPostForm, AnimalPostForm, FeedPostForm, AnimalTypeForm
from shop_app.models import Animal, AnimalType, Feed


class AnimalList(ListView):
    template_name = 'shop_app/animal_list.html'
    model = Animal
    context_object_name = 'animal_list'

    def get_context_data(self, **kwargs):
        context = super(AnimalList, self).get_context_data(**kwargs)
        # sort animals by rank
        context['animals'] = Animal.objects.annotate(rank=Avg('comment__mark')).order_by('-rank')
        return context


class AnimalCreateView(CreateView):
    form_class = AnimalPostForm
    template_name = 'shop_app/create_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class AnimalDetails(DetailView):
    template_name = 'shop_app/animal_detail.html'
    context_object_name = 'animal'
    model = Animal


class AnimalUpdateView(UpdateView):
    form_class = AnimalPostForm
    model = Animal
    template_name = 'shop_app/create_form.html'
    success_url = '/shop/'


class FeedList(ListView):
    template_name = 'shop_app/feed_list.html'
    model = Feed
    context_object_name = 'feeds'

    def get_context_data(self, **kwargs):
        context = super(FeedList, self).get_context_data(**kwargs)
        # sort animals by rank
        context['feeds'] = Feed.objects.all()
        return context


class FeedDetails(DetailView):
    template_name = 'shop_app/feed_detail.html'
    context_object_name = 'feed'
    model = Feed


class FeedCreateView(CreateView):
    form_class = FeedPostForm
    template_name = 'shop_app/create_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


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


class AnimalTypeList(ListView):
    template_name = 'shop_app/types_list.html'
    model = AnimalType
    context_object_name = 'types_list'

    def get_context_data(self, **kwargs):
        context = super(AnimalTypeList, self).get_context_data(**kwargs)
        context['types'] = AnimalType.objects.all()
        return context


class AnimalTypeCreateView(CreateView):
    form_class = AnimalTypeForm
    template_name = 'shop_app/create_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class AnimalTypeDetail(DetailView):
    template_name = 'shop_app/type_detail.html'
    model = AnimalType
    context_object_name = 'type'


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        animals = Animal.objects.filter(breed__icontains=q)
        return render(request, 'shop_app/animal_list.html',
                      {'animals': animals})

    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
