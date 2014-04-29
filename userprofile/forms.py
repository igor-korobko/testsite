# -*- coding: utf-8 -*-
from django import forms
# from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.fields import CharField
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

    login = forms.CharField(label="Логин", max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин", "required": "required" }))
    password = forms.CharField(label="Пароль", max_length=60, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль", "required": "required" }))


class UserProfileForm(forms.ModelForm):
    # about = forms.Field(required=False)
    # photo = forms.ImageField(required=False)

    class Meta:
        model = MyUserModel
        fields = ("about", "photo")
        widgets = {"about": forms.Textarea(attrs={"class": "form-control", }),
                   "photo": forms.FileInput(attrs={"class": "form-control", })}
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
        help_texts = {"username": "", }


class RegisterForm(UserCreationForm):

    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Повторите пароль", required="", widget=forms.PasswordInput(attrs={"class": "form-control"}))

