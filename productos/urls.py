from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView


urlpatterns = [
    path('', ProductoListView.as_view(), name='productos-list'),
    path('crear/', ProductoCreateView.as_view(), name='productos-create'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='productos-update'),


]