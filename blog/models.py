from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_extensions.db.fields import AutoSlugField
from ckeditor.fields import RichTextField
from slugify import slugify


def custom_slugify(value):
    return slugify(value, separator='-', allow_unicode=True)

class Post(models.Model):
    POST_PUBLISHED = 'pub'
    POST_DRAFT = 'drf'

    STATUS_CHOICES = (
        (POST_PUBLISHED, 'published'),
        (POST_DRAFT, 'draft'),
    )

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=['title'], unique=True, allow_unicode=True, slugify_function=custom_slugify)
    description = RichTextField()
    author = models.ForeignKey(to=get_user_model(), related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/post_image/', blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=POST_DRAFT)
    active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    