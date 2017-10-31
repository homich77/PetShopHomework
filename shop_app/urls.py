from django.conf.urls import url
from django_filters.views import FilterView

from shop_app.filters import AnimalFilter
from . import views

urlpatterns = [
    url(r'^$', views.AnimalList.as_view(), name='animal_list'),
    url(r'^(?P<pk>\d+)/$', views.AnimalDetails.as_view(), name='animal_detail'),
    url(r'^create/$', views.AnimalCreateView.as_view(), name='animal_create'),
    url(r'^(?P<pk>\d+)/update/$', views.AnimalUpdateView.as_view(), name='update_animal'),

    url(r'^feed/$', views.FeedList.as_view(), name='feed_list'),
    url(r'^feed/create/$', views.FeedCreateView.as_view(), name='feed_create'),
    url(r'^feed/(?P<pk>\d+)/$', views.FeedDetails.as_view(), name='feed_detail'),

    url(r'^types/$', views.AnimalTypeList.as_view(), name='types_list'),
    url(r'^types/(?P<pk>\d+)/$', views.AnimalTypeDetail.as_view(), name='type_detail'),
    url(r'^types/create/$', views.AnimalTypeCreateView.as_view(), name='type_create'),

    url(r'^(?P<pk>\d+)/new_comment/$', views.CommentAddView.as_view(), name='add_comment'),

    url(r'^filter/$', FilterView.as_view(filterset_class=AnimalFilter, template_name='search/animal_filter.html'),
        name='filter'),
    url(r'^search/$', views.search),
]
