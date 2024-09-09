from django.db import models
from django.contrib.auth.models import User

class ProyectoPortafolio(models.Model):
    perfil = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proyectos")
    nombre_proyecto = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100, blank=True, null=True)
    descripcion_proyecto = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    actividades_realizadas = models.TextField()
    archivos_adjuntos = models.FileField(upload_to='portafolio/', blank=True, null=True)
    enlace_externo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre_proyecto

class CurriculumVitae(models.Model):
    perfil = models.OneToOneField(User, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='curriculums/', blank=True, null=True)

    def __str__(self):
        return f"Currículum de {self.perfil.username}"

class Curso(models.Model):
    perfil = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cursos")
    nombre_curso = models.CharField(max_length=100)
    descripcion_curso = models.TextField(blank=True)
    organizacion = models.CharField(max_length=100, blank=True, null=True)
    enlace_curso = models.URLField(blank=True, null=True)
    imagen_curso = models.ImageField(upload_to='cursos/', blank=True, null=True)

    def __str__(self):
        return self.nombre_curso


# TODO: Cambiar el nombre de los modelos y sus atributos a ingles(solo he cambiado el nombre de PortfolioProject pero no sus atributos) y no he hecho migraciones con el nuevo nombre
# class PortfolioProject(models.Model):
#     profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
#     project_name = models.CharField(max_length=100)
#     client = models.CharField(max_length=100, blank=True, null=True)
#     project_description = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)
#     activities_done = models.TextField()
#     attached_files = models.FileField(upload_to='portfolio/', blank=True, null=True)
#     external_link = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return self.project_name

# class Resume(models.Model):
#     profile = models.OneToOneField(User, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='resumes/', blank=True, null=True)

#     def __str__(self):
#         return f"Resume of {self.profile.username}"

# class Course(models.Model):
#     profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
#     course_name = models.CharField(max_length=100)
#     course_description = models.TextField(blank=True)
#     organization = models.CharField(max_length=100, blank=True, null=True)
#     course_link = models.URLField(blank=True, null=True)
#     course_image = models.ImageField(upload_to='courses/', blank=True, null=True)

#     def __str__(self):
#         return self.course_name