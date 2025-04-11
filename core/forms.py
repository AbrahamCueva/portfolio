from django import forms
from .models import BlogPost
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Tu correo'})
    )
    asunto = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Asunto'})
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Mensaje', 'rows': 5})
    )

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'author', 'description', 'tags', 'content']
