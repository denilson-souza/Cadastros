from django.urls import path
from CadasrtroCliente import views

urlpatterns = [
    path('', views.index, name="index"),
]
