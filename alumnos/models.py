from django.db import models

class Generaciones(models.Model):
    año = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.año)

class Escuela(models.Model):
    NIVEL_CHOICES = [
        ('preescolar', 'Preescolar'),
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
        ('bachillerato', 'Bachillerato'),
        ('universidad', 'Universidad'),
        ('maestria', 'Maestría'),
    ]

    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    generacion = models.ForeignKey(Generaciones, on_delete=models.CASCADE, related_name='escuelas')

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    MES_CHOICES = [
        ('enero', 'Enero'),
        ('febrero', 'Febrero'),
        ('marzo', 'Marzo'),
        ('abril', 'Abril'),
        ('mayo', 'Mayo'),
        ('junio', 'Junio'),
        ('julio', 'Julio'),
        ('agosto', 'Agosto'),
        ('septiembre', 'Septiembre'),
        ('octubre', 'Octubre'),
        ('noviembre', 'Noviembre'),
        ('diciembre', 'Diciembre'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Grupo/Licenciatura")
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='grupos')
    generacion = models.ForeignKey(Generaciones, on_delete=models.CASCADE, related_name='grupos')
    mes_graduacion = models.CharField(max_length=20, choices=MES_CHOICES, blank=True, null=True, verbose_name="Mes de Graduación")

    def __str__(self):
        return self.nombre
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Alumno")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono", blank=True, null=True)
    folio_camara = models.CharField(max_length=50, verbose_name="Folio de Cámara", blank=True, null=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='alumnos')
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='alumnos')
    generacion = models.ForeignKey(Generaciones, on_delete=models.CASCADE, related_name='alumnos')

    def __str__(self):
        return self.nombre