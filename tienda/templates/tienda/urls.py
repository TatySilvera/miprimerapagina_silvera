from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar/', views.buscar_producto, name='buscar'),
    path('agregar-neceser/', views.agregar_neceser, name='agregar_neceser'),
]