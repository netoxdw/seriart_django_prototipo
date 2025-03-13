from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tag_description', 'precio', 'stock')
    search_fields = ('nombre', 'tag_description')
    list_filter = ('precio', 'stock')

