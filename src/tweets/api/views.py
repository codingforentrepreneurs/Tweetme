from rest_framework import generics


from tweets.models import Tweet
from .serializers import TweetModelSerializer


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        return Tweet.objects.all()