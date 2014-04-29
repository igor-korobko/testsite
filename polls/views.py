# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from polls.forms import VoteForm, CommentForm
from polls.models import Cookie, Comments
from django.contrib.auth import authenticate, login, get_user, logout
import functions
from userprofile.forms import LoginForm


def index(request):
    cookies = Cookie.objects.all().order_by('-rating')[:3]
    result = functions.get_all_forms(request, cookies)
    return render(request, "polls/index.html", result)


def cookies_(request):
    cookies = Cookie.objects.all()
    result = functions.get_all_forms(request, cookies)
    return render(request, "polls/cookies.html", result)


def search(request):
    if 'search' in request.POST:
        cookies = Cookie.objects.filter(name=request.POST['search'])
        result = functions.get_all_forms(request, cookies)
        return render(request, "polls/cookies.html", result)
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


def vote(request):
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
                if get_user(request) not in cookie_obj.user.all():
                    # // если такое есть, то записываем
                    if request.POST["rating"] in all_values:
                        cookie_obj.rating = old_rating + int(request.POST["rating"])
                        cookie_obj.user.add(get_user(request))
                        cookie_obj.save()
                        vote_form.save()

        if len(request.POST["comment"]) > 0:
            comment_obj = Comments(cookie_id=cookie_obj, user_id=get_user(request))
            comment_form = CommentForm(request.POST, instance=comment_obj)
            if comment_form.is_valid():
                cookie_obj.user.add(get_user(request))
                cookie_obj.save()
                comment_form.save()



        # cookie_obj = get_object_or_404(Cookie, pk=request.POST['cookie_id'])
        # cookie_obj.rating += int(request.POST['choice'])
        # cookie_obj.user.add(get_user(request))
        # cookie_obj.save()
        # if len(request.POST['comment']) > 0:
        #     comment_obj = Comments(comment=request.POST['comment'], user_id=get_user(request), cookie_id=cookie_obj)
        #     comment_obj.save()
        # # r = Relations(user_id=get_user(request), cookie_id=p)
        # # r.save()
        # return render(request, "polls/cookies.html" )
    return redirect(request.META['HTTP_REFERER'])


