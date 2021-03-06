from django.conf.urls import url

from projectbase import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registrar/', views.registrar_imovel, name='registrar'),
    url(r'^registrarImovel/$', views.registrar_imovel, name='registrar_imovel'),
    url(r'^sucesso/$', views.sucesso_registro, name='sucesso_registro'),
    url(r'^about/$', views.about, name='about'),
]