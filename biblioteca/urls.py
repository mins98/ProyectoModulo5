import imp
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('bibliotecas/create_list', views.BibliotecaCreateView.as_view()),
    path('materiales/create_list', views.MaterialBibliograficoCreateView.as_view()),
    path('materiales/delete/<int:pk>', views.MaterialBibliograficoGetAndDeleteView.as_view()),
    path('prestamos/create_list', views.PrestamoCreateView.as_view()),
    path('prestamos/devolver', views.devolver_prestamo),
]