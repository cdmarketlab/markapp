from django.urls import path

from . import views

urlpatterns = [
    path('registro', views.registro, name='registro'),
    path('nuevoregistro', views.nuevoRegistro, name='nuevoRegistro'),
    path('validaUser', views.valida_user, name='validaUser'),
]