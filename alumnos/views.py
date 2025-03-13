from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Generaciones, Escuela, Grupo, Alumno

# Create your views here.

class GeneracionesListView(ListView):
    model = Generaciones
    template_name = 'alumnos/generaciones_list.html'
    context_object_name = 'generaciones'

class GeneracionesCreateView(CreateView):
    model = Generaciones
    template_name = 'alumnos/generaciones_form.html'
    fields = ['año']
    success_url = reverse_lazy('generaciones-list')

class GeneracionesUpdateView(UpdateView):
    model = Generaciones
    template_name = 'alumnos/generaciones_form.html'
    fields = ['año']
    success_url = reverse_lazy('generaciones-list')



class EscuelaListView(ListView):
    model = Escuela
    template_name = 'alumnos/escuela_list.html'
    context_object_name = 'escuelas'

    def get_queryset(self):
        generacion_id = self.kwargs['generacion_id']
        return Escuela.objects.filter(generacion_id=generacion_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generacion'] = Generaciones.objects.get(id=self.kwargs['generacion_id'])
        return context

class EscuelaCreateView(CreateView):
    model = Escuela
    template_name = 'alumnos/escuela_form.html'
    fields = ['nombre', 'ciudad', 'nivel']

    def get_generacion(self):
        """Obtiene la generación asociada desde la URL."""
        generacion_id = self.kwargs.get('generacion_id')
        return get_object_or_404(Generaciones, id=generacion_id)

    def get_context_data(self, **kwargs):
        """Agrega la generación al contexto para usarla en el template."""
        context = super().get_context_data(**kwargs)
        context['generacion'] = self.get_generacion()
        return context

    def form_valid(self, form):
        """Asigna la generación a la escuela antes de guardarla."""
        form.instance.generacion = self.get_generacion()
        return super().form_valid(form)

    def get_success_url(self):
        """Redirige a la lista de escuelas de la generación después de crear una escuela."""
        return reverse_lazy('escuelas-list', args=[self.get_generacion().id])

class EscuelaUpdateView(UpdateView):
    model = Escuela
    fields = ['nombre', 'ciudad', 'nivel']
    template_name = 'alumnos/escuela_form.html'

    def get_context_data(self, **kwargs):
        """Agrega la generación al contexto para usarla en el template."""
        context = super().get_context_data(**kwargs)
        context['generacion'] = self.object.generacion
        return context

    def get_success_url(self):
        """Redirige a la lista de escuelas de la generación después de actualizar una escuela."""
        return reverse_lazy('escuelas-list', args=[self.object.generacion.id])
    

class GrupoListView(ListView):
    model = Grupo
    template_name = 'alumnos/grupo_list.html'
    context_object_name = 'grupos'

    def get_queryset(self):
        escuela_id = self.kwargs.get('escuela_id')
        return Grupo.objects.filter(escuela_id=escuela_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        escuela = get_object_or_404(Escuela, id=self.kwargs.get('escuela_id'))
        context['escuela'] = escuela
        context['generacion'] = escuela.generacion  # Agregar la generación al contexto
        return context

class GrupoCreateView(CreateView):
    model = Grupo
    template_name = 'alumnos/grupo_form.html'
    fields = ['nombre', 'mes_graduacion']  # Agregar mes_graduacion

    def get_escuela(self):
        return get_object_or_404(Escuela, id=self.kwargs.get('escuela_id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        escuela = self.get_escuela()
        context['escuela'] = escuela
        context['generacion'] = escuela.generacion
        return context

    def form_valid(self, form):
        form.instance.escuela = self.get_escuela()
        form.instance.generacion = form.instance.escuela.generacion
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('grupos-list', args=[self.get_escuela().id])

class GrupoUpdateView(UpdateView):
    model = Grupo
    template_name = 'alumnos/grupo_form.html'
    fields = ['nombre', 'mes_graduacion']  # Agregar mes_graduacion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['escuela'] = self.object.escuela
        context['generacion'] = self.object.generacion
        return context

    def get_success_url(self):
        return reverse_lazy('grupos-list', args=[self.object.escuela.id])
    

class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumnos/alumno_list.html'
    context_object_name = 'alumnos'

    def get_queryset(self):
        grupo_id = self.kwargs.get('grupo_id')
        return Alumno.objects.filter(grupo_id=grupo_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo = get_object_or_404(Grupo, id=self.kwargs.get('grupo_id'))
        context['grupo'] = grupo
        context['escuela'] = grupo.escuela
        context['generacion'] = grupo.generacion
        return context

class AlumnoCreateView(CreateView):
    model = Alumno
    template_name = 'alumnos/alumno_form.html'
    fields = ['nombre', 'telefono', 'folio_camara']

    def get_grupo(self):
        return get_object_or_404(Grupo, id=self.kwargs.get('grupo_id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo = self.get_grupo()
        context['grupo'] = grupo
        context['escuela'] = grupo.escuela
        context['generacion'] = grupo.generacion
        return context

    def form_valid(self, form):
        grupo = self.get_grupo()
        form.instance.grupo = grupo
        form.instance.escuela = grupo.escuela
        form.instance.generacion = grupo.generacion
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('alumnos-list', args=[self.get_grupo().id])

class AlumnoUpdateView(UpdateView):
    model = Alumno
    template_name = 'alumnos/alumno_form.html'
    fields = ['nombre', 'telefono', 'folio_camara']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alumno = self.get_object()  # Obtiene el alumno que se está editando
        context['grupo'] = alumno.grupo  # Accede a la relación con Grupo
        context['escuela'] = alumno.grupo.escuela  # Accede a la escuela
        context['generacion'] = alumno.grupo.escuela.generacion  # Accede a la generación
        return context

    def get_success_url(self):
        return reverse_lazy('alumnos-list', args=[self.object.grupo.id])