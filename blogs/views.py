from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.

def home(request):
    featured_posts = Blogs.objects.filter(is_featured = True, status='Published').order_by('-updated_at')[:4]
    posts = Blogs.objects.filter(is_featured = False, status='Published').order_by('-updated_at')[:4]

    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
    }

    return render(request, 'home.html', context)


def post_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Blogs.objects.filter(category__slug=slug)

    featured_posts = Blogs.objects.filter(is_featured=True, status='Published')
    context = {
        'posts' : posts,
        'category' : category,
        'featured_posts' : featured_posts,
    }

    return render(request, 'post_by_category.html', context)


def single_blog(request, slug):

    single_post = get_object_or_404(Blogs, slug=slug)

    if request.method == 'POST':
        Comment_text = request.POST.get('comment')
        if Comment_text:
            Comment.objects.create(
                user = request.user,
                blog = single_post,
                comment = Comment_text

            )
            return redirect('single_blog', slug=slug)
        

    comments = Comment.objects.filter(blog=single_post)

    context = {
        'single_post' : single_post,
        'comments' : comments,
    }

    return render(request, 'single_blog.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    
    posts = Blogs.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body__icontains = keyword) , status='Published')

    context = {
        'posts' : posts,
        'keyword' : keyword,
    }

    return render(request, 'search.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form' : form,
    }

    return render(request, 'registration/register.html', context)



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('home')

    else:   
        form = AuthenticationForm()

    context = {
        'form' : form,
    }

    return render(request, 'registration/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('login')



def featured_posts(request):
    posts = Blogs.objects.filter(is_featured=True, status='Published').order_by('-updated_at')

    context = {
        'posts' : posts,
    }

    return render(request, 'post_by_category.html', context)


def recent_posts(request):
    posts = Blogs.objects.filter(is_featured=False, status='Published').order_by('-updated_at')

    context = {
        'posts' : posts,
    }

    return render(request, 'post_by_category.html', context)