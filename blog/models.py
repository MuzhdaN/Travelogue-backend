# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_gdnt3o', blank=True
    )
    location = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    trip_duration = models.PositiveIntegerField()
    place = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    saved_for_later = models.ManyToManyField(
        User, related_name='saved_posts', blank=True
    )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.id} {self.title}'
