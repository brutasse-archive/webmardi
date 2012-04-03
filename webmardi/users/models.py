from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    screen_name = models.CharField(max_length=255)
    token = models.TextField(blank=True)
    token_secret = models.TextField(blank=True)
    auth_user = models.OneToOneField(User, null=True)

    def __unicode__(self):
        return u'%s' % self.screen_name
