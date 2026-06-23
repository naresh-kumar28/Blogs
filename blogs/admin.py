from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'created_at')
admin.site.register(Category, CategoryAdmin)


class BlogsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    search_fields = ('title', 'short_description', 'blog_body','category__category_name', 'author__username', 'status')
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    list_editable = ('is_featured', 'status')
admin.site.register(Blogs, BlogsAdmin)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_heading', 'about_description')

    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'link')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'blog', 'comment', 'created_at')