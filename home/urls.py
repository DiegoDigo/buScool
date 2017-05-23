from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^pesquisa/$', views.Pesquisa, name='pesquisa'),
    url(r'^login/$',views.login, name='login'),
]
