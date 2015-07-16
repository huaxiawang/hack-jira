__author__ = 'hwang'
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^load_data/$', views.load_data, name='load_data'),
]