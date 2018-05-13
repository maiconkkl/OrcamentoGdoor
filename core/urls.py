from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.orcamentolist, name='index'),
    url(r'^create/$', views.orcamentocreate, name='create'),
    url(r'^(?P<id>[0-9]+)/$', views.orcamento, name='orcamento'),
]