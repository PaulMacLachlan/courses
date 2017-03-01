
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.create_course),
    url(r'^course/(?P<id>[0-9]+)/destroy$', views.destroy, name='courses-destroy'),
    url(r'^course/(?P<id>[0-9]+)/destroy_confirm$', views.destroy_confirm, name='courses-destroy_confirm'),
    # url(r'^no_delete$', views.no_delete),
    # url(r'^yes_delete$', views.yes_delete),
    url(r'^$', views.index),
    # url(r'^courses/destroy/(?P<id>\d+)$', views.destroy)
]
