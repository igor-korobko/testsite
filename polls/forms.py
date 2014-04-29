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


# class CookiePostForm(forms.Form):
#
#     class Medua:
#         model = Cookie
#
#     login = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
#     password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))

class VoteForm(forms.ModelForm):
    # CHOICES = (('1', 'First',), ('2', 'Second',))
    # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Cookie
        CHOICES = (('1', '1',), ('2', '2',), ('3', '3',), ('4', '4',), ('5', '5',))
        fields = ("rating", )
        widgets = {"rating": forms.RadioSelect(choices=CHOICES)}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ("comment",)
        widgets = {"comment": forms.Textarea(attrs={"placeholder": "Отзыв","id": "poll_comment", "class": "form-control"}), }