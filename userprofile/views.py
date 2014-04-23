from django.shortcuts import render


def user_(request):
    return render(request, "userprofile/user.html")#, result