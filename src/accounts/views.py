from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.views.generic import DetailView
# Create your views here.

from .models import UserProfile

User = get_user_model()

class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()
    
    def get_object(self):
        return get_object_or_404(
                    User, 
                    username__iexact=self.kwargs.get("username")
                    )



class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            user_profile, created = UserProfile.objects.get_or_create(user=request.user) # (user_obj, true)
            if toggle_user in user_profile.following.all():
                user_profile.following.remove(toggle_user)
            else:
                user_profile.following.add(toggle_user)
        return redirect("profiles:detail", username=username)
        # url = reverse("profiles:detail", kwargs={"username": username})
        # HttpResponseRedirect(url)