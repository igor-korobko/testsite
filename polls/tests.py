# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import request
from django.test import TestCase
from models import Cookie, Comments
from forms import VoteForm


def create_cookie():
    cookie = Cookie()
    cookie.rating = 11
    cookie.name = "название"
    cookie.description = "описание"
    cookie.save()
    return cookie


def create_user():
    user = User()
    user.username = 'user'
    user.set_password("user")
    user.save()
    return user


class VoteViewTests(TestCase):

 # проверка наращивания голосов
    def test_vote_increment(self):
        user = create_user()
        cookie = create_cookie()
        cookie_id = cookie.pk
        cookie_rating = cookie.rating
        increment_value = int(VoteForm.Meta.CHOICES[0][0])
        response = self.client.post(reverse('polls:vote'), {'rating': increment_value,
                                                            'vote_btn': 'vote_btn',
                                                            'cookie_id': cookie_id,
                                                            "user": user,
                                                            })

        self.assertEqual(cookie.rating, increment_value+cookie_rating)



