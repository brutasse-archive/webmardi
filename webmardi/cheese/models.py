from django.db import models

from ..users.models import User


class Cheese(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cheese')
    description = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name

    def like_count(self):
        return self.tastes.filter(like=True).count()

    def dislike_count(self):
        return self.tastes.filter(like=False).count()


class Taste(models.Model):
    cheese = models.ForeignKey(Cheese, related_name='tastes')
    user = models.ForeignKey(User)
    like = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s's taste of %s" % (self.user, self.cheese)

    class Meta:
        unique_together = ('cheese', 'user')
