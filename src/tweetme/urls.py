"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from accounts.views import UserRegisterView

from hashtags.api.views import TagTweetAPIView
from hashtags.views import HashTagView
from tweets.api.views import SearchTweetAPIView
from tweets.views import TweetListView
from .views import home, SearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls), #admin/
    url(r'^$', TweetListView.as_view(), name='home'), #/
    url(r'^search/$', SearchView.as_view(), name='search'), #/
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    url(r'^tweet/', include('tweets.urls', namespace='tweet')),
    url(r'^api/tags/(?P<hashtag>.*)/$', TagTweetAPIView.as_view(), name='tag-tweet-api'), 
    url(r'^api/search/$', SearchTweetAPIView.as_view(), name='search-api'), 
    url(r'^api/tweet/', include('tweets.api.urls', namespace='tweet-api')),
    url(r'^api/', include('accounts.api.urls', namespace='profiles-api')),
    url(r'^register/$', UserRegisterView.as_view(), name='register'), #/
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('accounts.urls', namespace='profiles')),
]


if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))