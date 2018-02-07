from django.conf.urls import url
from . import views
from django.conf.urls import include

app_name = 'meCampus'


urlpatterns = [
    url(r'^$', views.index, name='index'),



]
