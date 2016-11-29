from django.shortcuts import render

# Create your views here.

# Create


#Update

#Delete

#List / Search

#Retrieve
def tweet_detail_view(request, id=1):
    return render(request, "tweets/detail_view.html", {})


def tweet_list_view(request):
    return render(request, "tweets/list_view.html", {})