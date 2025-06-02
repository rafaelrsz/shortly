from django.db import models
from .shorturl import ShortURL

class Click(models.Model):
    short_url = models.ForeignKey(ShortURL, on_delete=models.CASCADE, related_name='clicks')
    clicked_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    referrer = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Click on {self.short_url.short_code} at {self.clicked_at}"