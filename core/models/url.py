from django.db import models

class Url(models.Model):
    address = models.TextField()
    slug = models.SlugField(max_length=20, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.slug} -> {self.address}"