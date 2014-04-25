# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from polls.models import Cookie, Comments
from django.contrib.auth import authenticate, login, get_user, logout
import functions
from userprofile.forms import LoginForm


def index(request):
    cookies = Cookie.objects.all().order_by('-rating')[:3]
    result = functions.get_vote_form(request, cookies)
    form = LoginForm()
    result.update({"form": form})
    return render(request, "polls/index.html", result)


def cookies_(request):
    cookies = Cookie.objects.all()
    result = functions.get_vote_form(request, cookies)
    return render(request, "polls/cookies.html", result)


def search(request):
    if 'search' in request.POST:
        cookies = Cookie.objects.filter(name=request.POST['search'])
        result = functions.get_vote_form(request, cookies)
        return render(request, "polls/cookies.html", result)
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


def vote(request):
    if 'choice' in request.POST:
        cookie_obj = get_object_or_404(Cookie, pk=request.POST['cookie_id'])
        cookie_obj.rating += int(request.POST['choice'])
        cookie_obj.user.add(get_user(request))
        cookie_obj.save()
        if len(request.POST['comment']) > 0:
            comment_obj = Comments(comment=request.POST['comment'], user_id=get_user(request), cookie_id=cookie_obj)
            comment_obj.save()
        # r = Relations(user_id=get_user(request), cookie_id=p)
        # r.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


