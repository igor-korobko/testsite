from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user


def user_(request):
    user=get_user(request)
    user.get_profile()
    # User.profile = property(user.get_profile())
    return render(request, "userprofile/user.html")#, result