from .models import *

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_socialLink(request):
    sociallinks = SocialLink.objects.all()
    return dict(sociallinks=sociallinks)