from django.contrib import admin
from .models import AboutMe, Skill, Stat, Experience, Education, ContactInfo, MensajeContacto, HomeContent, PortfolioProject, BlogCategory, BlogPost, SiteSetting
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.utils.translation import gettext_lazy as _

class HomeContentForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = HomeContent
        fields = '__all__'

@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    form = HomeContentForm
    list_display = ('nombre', 'saludo', 'texto_boton')
    fieldsets = (
        ("Información principal", {
            'fields': ('saludo', 'nombre', 'descripcion', 'imagen')
        }),
        ("Botón", {
            'fields': ('texto_boton', 'enlace_boton')
        }),
    )

class AboutForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = AboutMe
        fields = '__all__'

@admin.register(AboutMe)
class AboutAdmin(admin.ModelAdmin):
    form = AboutForm
    list_display = ('nombre', 'apellido', 'edad', 'freelance')
    fieldsets = (
        ('Datos personales', {
            'fields': ('nombre', 'apellido', 'edad', 'nacionalidad', 'freelance', 'foto')
        }),
        ('Contacto', {
            'fields': ('direccion', 'telefono', 'email', 'skype', 'idiomas')
        }),
        ('Descripción', {
            'fields': ('descripcion', 'cv')
        }),
    )

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'lenguajes')
    search_fields = ('titulo', 'cliente', 'lenguajes')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'telefono')
    
@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha')
    search_fields = ('nombre', 'email', 'asunto', 'mensaje')
    list_filter = ('fecha',)
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    search_fields = ['title', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'image', 'category', 'description', 'tags')
        }),
        (_('Contenido'), {
            'fields': ('content',)
        }),
    )

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory)
admin.site.register(Skill)
admin.site.register(Stat)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(SiteSetting)