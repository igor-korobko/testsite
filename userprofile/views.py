from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import get_user
# from forms import MyUserProfileForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from models import MyUserModel
from django.core.urlresolvers import reverse


def user_(request):
    user = get_user(request)
    if not user.is_anonymous():
        if 'save' in request.POST:
            try:
                profile = MyUserModel.objects.get(user=user)
                profile.about = request.POST["about"]
                if 'photo' in request.FILES:
                    profile.photo = request.FILES["photo"]

            except(MyUserModel.DoesNotExist):
                profile = MyUserModel(about=request.POST["about"], photo=request.POST["photo"], user=user)

            profile.save()

            user_info = User.objects.get(pk=user.pk)

            user_info.first_name = request.POST["first_name"]
            user_info.last_name = request.POST["last_name"]
            user_info.email = request.POST["email"]
            if len(request.POST["password"]) > 0:
                user_info.set_password(request.POST["password"])
            user_info.save()
        else:
            profile = MyUserModel.objects.get_or_create(user=user)

        return render(request, "userprofile/user.html", {"prof": profile})
    else:
        return HttpResponseRedirect(reverse('polls:index'))


def public_(request, user_name):
    user = get_user(request)
    if not user.is_anonymous():
        pub_user = get_object_or_404(User, username=user_name)
        try:
            profile = MyUserModel.objects.get(user=pub_user)
        except(MyUserModel.DoesNotExist):
            profile = MyUserModel()
        return render(request, "userprofile/public.html", {"prof": profile, "pub_user": pub_user})
    else:
        return HttpResponseRedirect(reverse('polls:index'))

