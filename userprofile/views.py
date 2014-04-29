# -*- coding: utf-8 -*-
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.forms.models import modelformset_factory
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user, login, authenticate, logout
from forms import LoginForm, UserProfileForm, UserForm, RegisterForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from models import MyUserModel
from django.core.urlresolvers import reverse
from polls import functions
from polls.models import Cookie
from django import forms
from userprofile.forms import RegisterForm


def login_(request):
    # message = "sss"
    if request.method == 'POST':
        formset = LoginForm(request.POST)
        if formset.is_valid():
            user = authenticate(username=request.POST['login'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
            #     message = "is_active"
            # else:
            #     message = "Не верный логин или пароль"
    return redirect(reverse('polls:index'))
    # -----------------------------------------------------------
    # if 'login' in request.POST and 'pwd' in request.POST:
    #     log = request.POST['login']
    #     pwd = request.POST['pwd']
    #     user = authenticate(username=log, password=pwd)
    #     message = ""
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #     else:
    #         message = "Не верный логин или пароль"
    #
    #     cookies = Cookie.objects.all()
    #     result = functions.get_vote_form(request, cookies)
    #     result.update({'msg': message})
    #     return render(request, "polls/index.html", result)
    # else:
    #     return HttpResponseRedirect(reverse('polls:index'))


def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:index'))


def user_(request):

    # user = User.objects.get(pk=get_user(request).pk)
    # u_profile = MyUserModel.objects.get(user=user)
    # profile_form = MultiUserForm(instance=u_profile)
    # return render(request, 'userprofile/user.html', {'profile_form': profile_form})

    user = User.objects.get(pk=get_user(request).pk)
    try:
        u_profile = MyUserModel.objects.get(user=user)
    except(Exception):
        u_profile = MyUserModel(user=user)
    if request.method == "POST":

        profile_form = UserProfileForm(request.POST, request.FILES, instance=u_profile)
        if profile_form.is_valid():
            profile_form.save()

        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save(commit=False)
            if "password" in request.POST:
                user.set_password(request.POST["password"])
            user_form.save()

    else:
        profile_form = UserProfileForm(instance=u_profile)
        user_form = UserForm(instance=user)

    return render(request, 'userprofile/user.html', {'profile_form': profile_form, 'user_form': user_form})
    # ----------------------------------------------------------------------------------------------------------
    # user = get_user(request)
    # if not user.is_anonymous():
    #     if 'save' in request.POST:
    #         try:
    #             profile = MyUserModel.objects.get(user=user)
    #             # msg = "get"
    #         except(MyUserModel.DoesNotExist):
    #             profile = MyUserModel(about=request.POST["about"], photo=request.POST["photo"], user=user)
    #             # msg = "new"
    #         else:
    #             profile.about = request.POST["about"]
    #             if 'photo' in request.FILES:
    #                 profile.photo = request.FILES["photo"]
    #
    #         profile.save()
    #
    #         user_info = User.objects.get(pk=user.pk)
    #
    #         user_info.first_name = request.POST["first_name"]
    #         user_info.last_name = request.POST["last_name"]
    #         user_info.email = request.POST["email"]
    #         if len(request.POST["password"]) > 0:
    #             user_info.set_password(request.POST["password"])
    #         user_info.save()
    #     else:
    #         profile = MyUserModel.objects.get_or_create(user=user)
    #         # msg = profile[0].user
    #
    #     return render(request, "userprofile/user.html", {"prof": profile[0]})
    # else:
    #     return HttpResponseRedirect(reverse('polls:index'))


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


def register_(request):

    if request.method == "POST":
        userCrtForm = RegisterForm(request.POST)
        if userCrtForm.is_valid():
            userCrtForm.save()
            return redirect('polls:index')
    else:
        userCrtForm = RegisterForm()
        return render(request, "userprofile/register.html", {"userCrtForm": userCrtForm})

