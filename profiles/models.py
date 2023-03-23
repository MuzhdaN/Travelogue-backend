from django.db import models
from django.db.models.signals import post_save

# import standard django user model to be refrenced in the custom models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_ns4oad'
    )

    # return profile instances in reverse order
    class Meta:
        ordering = ['-created_at']

    # who the profile owner is
    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """ Create a profile every time a user is created """
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)