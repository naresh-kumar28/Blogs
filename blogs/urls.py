from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.post_by_category, name='post_by_category'),
    path('blog/<slug:slug>/', views.single_blog, name='single_blog'),
    path('search/', views.search, name='search'),

    #authentication
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    #view all
    path('featured-posts/', views.featured_posts, name='featured_posts'),
    path('recent-posts/', views.recent_posts, name='recent_posts'),
]
