from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    content_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #photo = models.ImageField(upload_to=)
    is_published = models.BooleanField(default=True)


