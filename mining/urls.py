__author__ = 'hwang'
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^load_data/$', views.load_data, name='load_data'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^cases/$', views.cases, name='cases'),
    url(r'^correlation/$', views.correlation, name='correlation'),
    url(r'^#/corrrelation/$', views.correlation, name='correlation'),
]