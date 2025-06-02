from django.db import models
from django.contrib.auth.models import User
from .urltag import URLTag

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(URLTag, blank=True)

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"
