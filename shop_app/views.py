from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, TemplateView

from shop_app.forms import CommentPostForm, AnimalPostForm, FeedPostForm, AnimalTypeForm
from shop_app.models import Animal, AnimalType, Feed, Cart, OrderAnimal


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
    success_url = '/'


class FeedList(ListView):
    template_name = 'shop_app/feed_list.html'
    model = Feed
    context_object_name = 'feeds'

    def get_context_data(self, **kwargs):
        context = super(FeedList, self).get_context_data(**kwargs)
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
    success_url = '/'

    def post(self, request, pk):
        animal = Animal.objects.get(pk=pk)
        form = CommentPostForm(request.POST,
                               request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.animal = animal
            form.save()
            return redirect('animal_list')
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


class CartView(ListView):
    model = Cart
    context_object_name = 'order_list'
    template_name = 'shop_app/cart.html'

    def get_queryset(self):
        cart = Cart.objects.filter(status='open')
        if cart:
            animals_order = OrderAnimal.objects.filter(order=cart)
            return animals_order
        return False

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        cart = Cart.objects.filter(status='open')
        if cart:
            animals_order = OrderAnimal.objects.filter(order=cart)
            sum = 0
            for animal in animals_order:
                sum += animal.total_sum
            context['sum'] = sum
        return context


class CartPayView(TemplateView):
    template_name = 'shop_app/cart.html'

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(status='open')
        if cart:
            cart.status = 'closed'
            cart.save()
        return redirect('cart')


class AnimalOrderView(TemplateView):
    template_name = 'shop_app/animal_list.html'

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get_or_create(status='open')[0]
        OrderAnimal.objects.create(order=cart, animal_id=request.POST['animal_id'],
                                   quantity=int(request.POST['quantity']))
        cart.save()
        return redirect('animal_list')


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        animals = Animal.objects.filter(breed__icontains=q)
        return render(request, 'shop_app/animal_list.html',
                      {'animals': animals})

    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
