from blogs.models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('slug',)


class AddBlogPost(forms.ModelForm):
    class Meta:
        model = Blogs
        exclude = ('slug', 'author')
        


class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups']



class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups']