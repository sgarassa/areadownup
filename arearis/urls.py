from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^file/add/$', views.add_file, name='add_file'),
    url(r'^file/adds/$', views.model_form_upload, name='model_form_upload'),
    url(r'^download/$', views.download, name='download'),
]
