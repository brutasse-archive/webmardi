import urlparse

from django.contrib.auth import login
from django.contrib.auth.models import User as AuthUser
from django.contrib.sites.models import RequestSite
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import simplejson as json

import twitter

from le_social.twitter import views

from .models import User


class Authorize(views.Authorize):
    def build_callback(self):
        site = RequestSite(self.request)
        query = ''
        if 'next' in self.request.GET:
            query = '?next=%s' % self.request.GET['next']
        return 'http://%s%s%s' % (site.domain, reverse('oauth_callback'), query)
authorize = Authorize.as_view()


class Callback(views.Callback):
    def error(self, message, exception=None):
        return HttpResponse(message)

    def success(self, auth):
        api = twitter.Twitter(auth=auth)
        user = api.account.verify_credentials()
        dbuser, created = User.objects.get_or_create(
            screen_name=user['screen_name']
        )
        if not dbuser.auth_user:
            dbuser.auth_user = AuthUser.objects.create(
                username=user['screen_name'],
                password='!',
            )
            dbuser.auth_user.save()
        dbuser.token = auth.token
        dbuser.token_secret = auth.token_secret
        dbuser.save()
        dbuser.auth_user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, dbuser.auth_user)
        url = urlparse.urlparse(self.request.GET.get('next', reverse('cheese_list')))[2]
        return redirect(url)
callback = Callback.as_view()
