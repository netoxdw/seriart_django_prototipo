from django.urls import path
from .views import GeneracionesListView, GeneracionesCreateView, GeneracionesUpdateView, EscuelaListView, EscuelaCreateView, EscuelaUpdateView, GrupoListView, GrupoCreateView, GrupoUpdateView, AlumnoListView, AlumnoCreateView, AlumnoUpdateView

urlpatterns = [
    path('', GeneracionesListView.as_view(), name='generaciones-list'),
    path('crear/', GeneracionesCreateView.as_view(), name='generaciones-create'),
    path('editar/<int:pk>/', GeneracionesUpdateView.as_view(), name='generaciones-update'),

    path('<int:generacion_id>/escuelas/', EscuelaListView.as_view(), name='escuelas-list'),
    path('<int:generacion_id>/escuelas/crear/', EscuelaCreateView.as_view(), name='escuelas-create'),
    path('escuelas/editar/<int:pk>/', EscuelaUpdateView.as_view(), name='escuelas-update'),

    path('<int:escuela_id>/grupos/', GrupoListView.as_view(), name='grupos-list'),
    path('<int:escuela_id>/grupos/crear/', GrupoCreateView.as_view(), name='grupos-create'),
    path('grupos/editar/<int:pk>/', GrupoUpdateView.as_view(), name='grupos-update'),

    path('<int:grupo_id>/alumnos/', AlumnoListView.as_view(), name='alumnos-list'),
    path('<int:grupo_id>/alumnos/crear/', AlumnoCreateView.as_view(), name='alumnos-create'),
    path('alumnos/editar/<int:pk>/', AlumnoUpdateView.as_view(), name='alumnos-update'),
]