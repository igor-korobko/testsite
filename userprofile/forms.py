# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from models import MyUserModel

# from models import MyUserModel
#
#
# class MyUserProfileForm(forms.ModelForm):
#
#     class Meta:
#         fields = ("about", "photo")
#         model = MyUserModel


class LoginForm(forms.Form):

    login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = MyUserModel
        fields = ("about", "photo")
        widgets = {"about": forms.Textarea(attrs={"class": "form-control",}),
                   "photo": forms.FileInput(attrs={"class": "form-control",})}
        labels = {"about": "О себе", "photo": "Фото"}


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password")
        widgets = {"username": forms.TextInput(attrs={"class": "form-control"}),
                    "email": forms.TextInput(attrs={"class": "form-control"}),
                    "first_name": forms.TextInput(attrs={"class": "form-control"}),
                    "last_name": forms.TextInput(attrs={"class": "form-control"}),
                    "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }
        labels = {"username": "Логин",
                    "password": "Пароль",
                    "email": "Почта",
                    "first_name": "Имя",
                    "last_name": "Фамилия",
        }
        help_texts = {"username": "",}

    def save_password(self, user, password):
        user.save_password(password)