from django.conf import settings
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile') # user.profile 
    following   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by') 
    # user.profile.following -- users i follow
    # user.followed_by -- users that follow me -- reverse relationship

    def __str__(self):
        return str(self.following.all().count())