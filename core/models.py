from django.db import models
from .utils import create_shortened_url

class Shortener(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    followed = models.PositiveIntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return f'{self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)
