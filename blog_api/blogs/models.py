from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='blogs')
    slug = models.SlugField(blank=True)
    published_date = models.DateField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.title)

            super().save(*args, **kwargs)

    def __str__(self):
        return self.title