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


def create_comment(user, cookie):
    comment = Comments(user_id=user, cookie_id=cookie)
    return comment


def create_user():
    user = User()
    user.username = 'user'
    user.set_password("user")
    user.save()
    return user


class VoteViewTests(TestCase):

 # проверка наращивания голосов анонимусом
    def test_vote_increment_anonymous(self):
        user = create_user()
        cookie = create_cookie()
        cookie_id = cookie.pk
        cookie_rating = cookie.rating
        increment_value = int(VoteForm.Meta.CHOICES[0][0])
        response = self.client.post(reverse('polls:vote'), {'rating': increment_value,
                                                            'vote_btn': 'vote_btn',
                                                            'cookie_id': cookie_id,
                                                            })
        new_cookie = Cookie.objects.get(pk=cookie_id)
        self.assertNotEqual(new_cookie.rating, increment_value+cookie_rating)

# проверка сохраниения комментариев анонимусом
    def test_comment_saving_anonymous(self):
        cookie = create_cookie()
        cookie_id = cookie.pk
        comment_text = "Comment text"
        response = self.client.post(reverse('polls:vote'), {'comment': comment_text,
                                                            'vote_btn': 'vote_btn',
                                                            'cookie_id': cookie_id,
                                                            })
        try:
            new_comment = Comments.objects.get(cookie_id=cookie_id)
        except(Exception):
            pass
        else:
            self.fail("Error permissions")

 # проверка наращивания голосов
    def test_vote_increment(self):
        user = create_user()
        cookie = create_cookie()
        cookie_id = cookie.pk
        cookie_rating = cookie.rating
        increment_value = int(VoteForm.Meta.CHOICES[0][0])
        self.client.login(username='user', password='user')
        response = self.client.post(reverse('polls:vote'), {'rating': increment_value,
                                                            'vote_btn': 'vote_btn',
                                                            'cookie_id': cookie_id,
                                                            })
        new_cookie = Cookie.objects.get(pk=cookie_id)
        self.assertEqual(new_cookie.rating, increment_value+cookie_rating)

 # проверка сохраниения комментариев
    def test_comment_saving(self):
        user = create_user()
        cookie = create_cookie()
        cookie_id = cookie.pk
        comment_text = "Comment text"
        self.client.login(username='user', password='user')
        response = self.client.post(reverse('polls:vote'), {'comment': comment_text,
                                                            'vote_btn': 'vote_btn',
                                                            'cookie_id': cookie_id,
                                                            })

        new_comment = Comments.objects.get(cookie_id=cookie_id, user_id=user.pk)
        self.assertEqual(new_comment.comment, comment_text)

 # неличие forms.vote_form.Meta.CHOICES
    def test_choices_existing(self):
        is_exist = False
        try:
            choices = VoteForm.Meta.CHOICES[0][0]
            is_exist = True
        except(Exception):
            pass
        self.assertEqual(is_exist, True)

