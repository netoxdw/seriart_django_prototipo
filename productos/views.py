from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'
    context_object_name = 'productos_agrupados'

    def get_queryset(self):
        """Agrupa los productos por tag_description."""
        productos = Producto.objects.all()
        productos_agrupados = {}
        for producto in productos:
            tag = producto.tag_description or "Sin etiqueta"  # Si no hay tag_description, se agrupa como "Sin etiqueta"
            if tag not in productos_agrupados:
                productos_agrupados[tag] = []
            productos_agrupados[tag].append(producto)
        return productos_agrupados

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    fields = ['nombre', 'tag_description', 'precio', 'stock']
    success_url = reverse_lazy('productos-list')

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'productos/producto_form.html'
    fields = ['nombre', 'tag_description', 'precio', 'stock']
    success_url = reverse_lazy('productos-list')

