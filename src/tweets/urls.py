from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    RetweetView,
    TweetCreateView,
    TweetDeleteView,
    TweetDetailView,
    TweetListView,
    TweetUpdateView
    )

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")), 
    url(r'^search/$', TweetListView.as_view(), name='list'), # /tweet/
    url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='detail'), # /tweet/1/
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update/
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
]

