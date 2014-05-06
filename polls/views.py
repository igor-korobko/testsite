# -*- coding: utf-8 -*-
from urllib import urlopen
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, get_object_or_404, redirect
from polls.forms import VoteForm, CommentForm
from polls.models import Cookie, Comments
from django.contrib.auth import get_user
# from social_auth.signals import pre_update
# from django.dispatch import receiver
from django.utils import translation
import functions


# @receiver(pre_update)
# def update_person_details(sender, **kwargs):
#     raise("qweqweqew")
#     person = kwargs.get('user')
#     details = kwargs.get('details')
#     load_person_avatar(sender, person, kwargs.get('response'))
#
#
# def load_person_avatar(sender, person, info):
#     image_url = None
#
#     if sender.name == 'twitter':
#         image_url = info.get('profile_image_url')
#         if not 'default_profile' in image_url:
#             image_url = image_url.replace('_normal', '_bigger')
#         else: # No real image
#             image_url = None
#     if image_url:
#         # try:
#             image_content = urlopen(image_url)
#
#             # Facebook default image check
#             if sender.name == 'facebook' and 'image/gif' in str(image_content.info()):
#                 return
#
#             image_name = default_storage.get_available_name(person.avatar.field.upload_to + '/' + str(person.id) + '.' + image_content.headers.subtype)
#             raise()
#             person.avatar.save(image_name, ContentFile(image_content.read()))
#             person.save()
#         # except Exception:
#         #     pass # Here we completely do not care about errors
        

def index(request):
    cookies = Cookie.objects.all().order_by('-rating')[:3]
    result = functions.get_all_forms(request, cookies)

    # li = get_language_info(get_language())
    # print(li['name'], li['name_local'], li['bidi'])
    # raise()
    # translation.activate("en")

    return render(request, "polls/index.html", result)


def cookies_(request):
    cookies = Cookie.objects.all()
    result = functions.get_all_forms(request, cookies)
    return render(request, "polls/cookies.html", result)


def search(request):
    if 'search' in request.POST:
        cookies = Cookie.objects.filter(name__contains=request.POST['search'])
        result = functions.get_all_forms(request, cookies)
        return render(request, "polls/cookies.html", result)
    else:
        return redirect(request.META['HTTP_REFERER'])


def vote(request):

    user = get_user(request)
    if not user.is_anonymous():
        if 'vote_btn' in request.POST:
            cookie_obj = get_object_or_404(Cookie, pk=request.POST['cookie_id'])

            if "rating" in request.POST:
                vote_form = VoteForm(request.POST, instance=cookie_obj)
                old_rating = cookie_obj.rating
                if vote_form.is_valid():
                    all_values = []
                    # // проверяем, полученное значение POST["rating"]
                    for radio_values in vote_form.Meta.CHOICES:
                        all_values.append(radio_values[0])
                    # // что бы ещё не голосовал
                    if user not in cookie_obj.user.all():

                        # // если такое есть, то записываем
                        if request.POST["rating"] in all_values:
                            cookie_obj.rating = old_rating + int(request.POST["rating"])
                            cookie_obj.user.add(user)
                            cookie_obj.save()
                            vote_form.save()

            if "comment" in request.POST:
                if len(request.POST["comment"]) > 0:
                    comment_obj = Comments(cookie_id=cookie_obj, user_id=user)
                    comment_form = CommentForm(request.POST, instance=comment_obj)
                    if comment_form.is_valid():
                        cookie_obj.user.add(user)
                        cookie_obj.save()
                        comment_form.save()

    if 'HTTP_REFERER' in request.META:
        path_to_redirect = request.META['HTTP_REFERER']
    else:
        path_to_redirect = "polls/index.html"

    return redirect(path_to_redirect)

