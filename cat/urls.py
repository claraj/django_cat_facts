from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='homepage'),
    url(r'^getfacts$', views.get_facts, name='get_facts')
 ]
