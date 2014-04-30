# -*- coding: utf-8 -*-
from django import forms
from models import Cookie, Comments


class VoteForm(forms.ModelForm):

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