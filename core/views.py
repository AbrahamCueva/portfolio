from django.shortcuts import render, redirect, get_object_or_404
from .models import AboutMe, PortfolioProject, HomeContent, ContactInfo, MensajeContacto, BlogPost
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.core.paginator import Paginator

def index(request):
    home = HomeContent.objects.first()
    context = {
        'home': home,
        'now': datetime.now(), 
        'body_class': 'home',
    }
    return render(request, 'core/index.html', context)

def about(request):
    about = AboutMe.objects.prefetch_related('skills', 'stats', 'experiences', 'educations').first()
    if about is None:
        return HttpResponse("No data found.")
    context = {
        'about': about,
        'now': datetime.now(), 
        'body_class': 'about',
    }
    return render(request, 'core/about.html', context)

def portfolio(request):
    proyectos = PortfolioProject.objects.all()
    context = {
        'proyectos': proyectos,
        'now': datetime.now(), 
        'body_class': 'portfolio', 
    }
    return render(request, 'core/portfolio.html', context)

def contacto(request):
    contacto = ContactInfo.objects.first()

    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            MensajeContacto.objects.create(
                nombre=nombre,
                email=email,
                asunto=asunto,
                mensaje=mensaje
            )
            return JsonResponse({'success': True, 'message': 'Mensaje enviado correctamente.'})
        else:
            return JsonResponse({'success': False, 'error': form.errors}, status=400)

    else:
        form = ContactForm()
        context = {
            'contacto': contacto,
            'form': form,
            'now': datetime.now(), 
            'body_class': 'contact',
        }
        return render(request, 'core/contact.html', context)

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj.object_list,
        'now': datetime.now(), 
        'body_class': 'blog', 
        'page_obj': page_obj,
    }
    
    return render(request, 'core/blog_list.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'post': post,
        'now': datetime.now(), 
        'body_class': 'blog-post',
    }
    return render(request, 'core/blog_detail.html', context)