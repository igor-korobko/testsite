# -*- coding: utf-8 -*-
from django import forms
from models import Cookie, Comments

# from models import MyUserModel
#
#
# class MyUserProfileForm(forms.ModelForm):
#
#     class Meta:
#         fields = ("about", "photo")
#         model = MyUserModel


class CookiePostForm(forms.Form):

    class Medua:
        model = Cookie

    login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))
    