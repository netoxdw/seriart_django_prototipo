from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumnos.urls')),
    path('productos/', include('productos.urls')),
]
