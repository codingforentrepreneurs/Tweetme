from django.conf.urls import url


from .views import TweetListView, TweetDetailView, tweet_detail_view

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='list'), # /tweet/
    #url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
]

