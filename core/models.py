from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class HomeContent(models.Model):
    saludo = models.CharField(max_length=100, verbose_name="Saludo (ej. ¡Hola!)")
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    descripcion = RichTextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to='home/', verbose_name="Imagen principal")
    texto_boton = models.CharField(max_length=50, default="Más sobre mí", verbose_name="Texto del botón")
    enlace_boton = models.URLField(default="/about", verbose_name="Enlace del botón")

    class Meta:
        verbose_name = "Contenido de Inicio"
        verbose_name_plural = "Contenido de Inicio"

    def __str__(self):
        return f"{self.nombre}"

class AboutMe(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    nacionalidad = models.CharField(max_length=100)
    freelance = models.BooleanField(default=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    skype = models.CharField(max_length=100)
    idiomas = models.CharField(max_length=200)
    descripcion = RichTextField()
    foto = models.ImageField(upload_to='about/', blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True, verbose_name="Archivo CV (PDF)")

    class Meta:
        verbose_name = "Sobre mí"
        verbose_name_plural = "Sobre mí"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Skill(models.Model):
    about = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='skills')
    nombre = models.CharField(max_length=100)
    porcentaje = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.porcentaje}%"

class Stat(models.Model):
    about = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='stats')
    titulo = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo}: {self.cantidad}"

class Experience(models.Model):
    about = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='experiences')
    titulo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    anio = models.CharField(max_length=100)
    descripcion = RichTextField()

    def __str__(self):
        return f"{self.titulo} - {self.empresa}"

class Education(models.Model):
    about = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name='educations')
    titulo = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    anio = models.CharField(max_length=100)
    descripcion = RichTextField()

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"

class PortfolioProject(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del proyecto")
    cliente = models.CharField(max_length=200, verbose_name="Cliente")
    lenguajes = models.CharField(max_length=200, verbose_name="Lenguajes/tecnologías")
    enlace = models.URLField(blank=True, null=True, verbose_name="Enlace del proyecto")
    imagen = models.ImageField(upload_to='portfolio/', verbose_name="Imagen destacada")
    descripcion = models.TextField(verbose_name="Descripción del proyecto")

    class Meta:
        verbose_name = "Proyecto de Portafolio"
        verbose_name_plural = "Proyectos de Portafolio"

    def __str__(self):
        return self.titulo

class ContactInfo(models.Model):
    titulo = models.CharField(max_length=200, default="Get in touch")
    subtitulo = models.CharField(max_length=200, default="Contact")
    mensaje_intro = RichTextField(verbose_name="Mensaje introductorio")
    
    email = models.EmailField(verbose_name="Correo de contacto")
    telefono = models.CharField(max_length=50, verbose_name="Número de teléfono")

    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Información de contacto"
        verbose_name_plural = "Información de contacto"

    def __str__(self):
        return "Sección Contacto"
    
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=150)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.asunto}"

class BlogCategory(models.Model):
    name = models.CharField("Nombre", max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField("Título", max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField("Imagen", upload_to='blog/')
    description = models.CharField("Descripción corta", max_length=500)
    content = RichTextField("Contenido")  # CKEditor
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name="Categoría")
    tags = models.CharField("Etiquetas", max_length=200)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última modificación", auto_now=True)
    author = models.CharField("Autor", max_length=100, default="admin")

    def __str__(self):
        return self.title

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="Mi Sitio")
    favicon = models.ImageField(upload_to='settings/', null=True, blank=True)

    def __str__(self):
        return "Configuración del Sitio"

    class Meta:
        verbose_name = "Configuración del Sitio"
        verbose_name_plural = "Configuración del Sitio"