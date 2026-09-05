from django.urls import path
from . import views

urlpatterns = [
    path('reservas/nueva/', views.reserva_create, name='reserva_create'),
]