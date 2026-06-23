from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import *
from .forms import *
from django.template.defaultfilters import slugify

# Create your views here.
def dashboard(request):
    posts = Blogs.objects.all().order_by('-updated_at')[:3]
    total_users = User.objects.count()

    context = {
        'posts' : posts,
        'total_users' : total_users,
    }

    return render(request, 'dashboard.html', context)


def category(request):
    return render(request, 'category.html')


def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            cat.slug = slugify(cat.category_name) + '-' +str(cat.id)
            cat.save()
            return redirect('category')

    form = CategoryForm()

    context = {
        'form' : form,
    }

    return render(request, 'add_category.html', context)


def edit_category(request, id):

    cat = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('category')

    form = CategoryForm(instance=cat)

    context = {
        'form' : form,
    }

    return render(request, 'edit_category.html', context)


def delete_category(request, id):
    cat = get_object_or_404(Category, id=id)
    cat.delete()
    return redirect('category')


def posts(request):
    posts = Blogs.objects.all().order_by('-updated_at')

    context = {
        'posts' : posts,
    }

    return render(request, 'posts.html', context)


def add_post(request):

    if request.method == 'POST':
        form = AddBlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.slug = slugify(post.title) + '-' + str(post.id)
            post.save()
            return redirect('posts')

    form = AddBlogPost()
    
    context = {
        'form' : form,
    }

    return render(request, 'add_post.html', context)


def edit_post(request, id):

    post = get_object_or_404(Blogs, id=id)

    if request.method == 'POST':
        form = AddBlogPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title) + '-' + str(post.id)
            post.save()
            return redirect('posts')

    form = AddBlogPost(instance=post)

    context = {
        'form' : form,
    }
    
    return render(request, 'edit_post.html', context)


def delete_post(request, id):
    post = get_object_or_404(Blogs, id=id).delete()
    return redirect('posts')


def users(request):
    users = User.objects.all()

    context = {
        'users' : users,
    }

    return render(request, 'users.html', context)


def add_user(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')

    form = UserAddForm()

    context = {
        'form' : form,
    }

    return render(request, 'add_user.html', context)


def edit_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')

    form = EditUserForm(instance=user)

    context = {
        'form' : form,
    }

    return render(request, 'edit_user.html', context)


def delete_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.user == user:
        return redirect('users')
    
    if user.is_superuser:
        return redirect('users')
    
    user.delete()

    return redirect('users')