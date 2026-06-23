from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

STATUS_CHOICES = [
    ('Draft', 'Draft'),
    ('Published', 'Published'),
]

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=500)
    blog_body = models.TextField()
    featured_image = models.ImageField(upload_to='uploads/%Y-%m-%d')
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


class About(models.Model):
    about_heading = models.CharField(max_length=100)
    about_description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading
    

class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.platform
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
