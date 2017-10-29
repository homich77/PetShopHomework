from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AnimalList.as_view(), name='animal_list'),
    url(r'^(?P<pk>\d+)/$', views.AnimalDetails.as_view(), name='animal_detail'),

    url(r'^types/$', views.TypeList.as_view(), name='types_list'),
    url(r'^types/(?P<pk>\d+)/$', views.TypeDetail.as_view(), name='type_detail'),

    url(r'^(?P<pk>\d+)/new_comment/$', views.CommentAddView.as_view(), name='add_comment'),
]