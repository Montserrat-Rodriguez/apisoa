from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from example import views

urlpatterns = [    
     #urls extra
     re_path(r'^/carrera_lista/$', views.CarreraList.as_view() ),
     re_path(r'^/carrera_detail/(?P<id>\d+)$', views.CarreraDetail.as_view() ),
     re_path(r'^/carreraview/$', views.CarreraListAll.as_view() ),          


     re_path(r'^/alumnos_lista/$', views.AlumnosList.as_view() ),
     re_path(r'^/alumnos_listanombre/$', views.AlumnostListNombre.as_view() ),
     re_path(r'^/alumnos_listaedad/$', views.AlumnostListEdad.as_view() ),
     re_path(r'^/alumnos_listacarrera/$', views.AlumnostListCarrera.as_view() ),
     re_path(r'^/alumnosview/$', views.AlumnostListAll.as_view() ),
     re_path(r'^/alumnos_detail/(?P<id>\d+)$', views.AlumnosDetail.as_view() ),
     re_path(r'^/alumnosviewdetail/(?P<id>\d+)$', views.AlumnosDetail.as_view() ),
     re_path(r'^/alumnosviewdetailnombre/(?P<nombre1>\w+)/$', views.AlumnostListNombre.as_view() ),
     re_path(r'^/alumnosviewdetailedad/(?P<edad1>\d+)/$', views.AlumnostListEdad.as_view() ),
     re_path(r'^/alumnosviewdetailcarrera/(?P<carrera1>\d+)/$', views.AlumnostListCarrera.as_view() ),

]