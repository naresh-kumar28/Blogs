from django.core.management.base import BaseCommand
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Regenerate slugs for Blogs using the full title and ensure uniqueness.'

    def handle(self, *args, **options):
        from blogs.models import Blogs

        def generate_unique_slug(model, instance, base_slug):
            slug = base_slug
            i = 1
            while model.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
                slug = f"{base_slug}-{i}"
                i += 1
            return slug

        qs = Blogs.objects.all()
        total = qs.count()
        self.stdout.write(f'Found {total} blog posts. Regenerating slugs...')
        for idx, obj in enumerate(qs, 1):
            base = slugify(obj.title)
            new_slug = generate_unique_slug(Blogs, obj, base)
            if obj.slug != new_slug:
                obj.slug = new_slug
                obj.save(update_fields=['slug'])
                self.stdout.write(f'[{idx}/{total}] Updated: {obj.title} -> {new_slug}')
            else:
                self.stdout.write(f'[{idx}/{total}] Skipped (unchanged): {obj.title}')
        self.stdout.write(self.style.SUCCESS('Slug regeneration complete.'))
