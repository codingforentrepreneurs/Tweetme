from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render
from django.views import View

def home(request):
    return render(request, "home.html", {})



User = get_user_model()

class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        qs = None
        if query:
            qs = User.objects.filter(
                    Q(username__icontains=query)
                )
        context = {"users": qs}
        return render(request, "search.html", context)