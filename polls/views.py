# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from polls.models import Cookie, Comments, Relations
from django.contrib.auth import authenticate, login, get_user, logout
import functions


def index(request):
    cookies = Cookie.objects.all().order_by('-rating')[:3]
    result = functions.get_vote_form(request, cookies)
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


def login_(request):

    if 'login' in request.POST and 'pwd' in request.POST:
        log = request.POST['login']
        pwd = request.POST['pwd']
        user = authenticate(username=log, password=pwd)
        message = ""
        if user is not None:
            if user.is_active:
                login(request, user)
        else:
            message = "Не верный логин или пароль"

        cookies = Cookie.objects.all()
        result = functions.get_vote_form(request, cookies)
        result.update({'msg': message})
        return render(request, "polls/index.html", result)
    else:
        return HttpResponseRedirect(reverse('polls:index'))


def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:index'))


def vote(request):
    if 'choice' in request.POST:
        p = get_object_or_404(Cookie, pk=request.POST['cookie_id'])
        p.rating += int(request.POST['choice'])
        p.save()
        if len(request.POST['comment']) > 0:
            c = Comments(comment=request.POST['comment'], user_id=get_user(request), cookie_id=p)
            c.save()
        r = Relations(user_id=get_user(request), cookie_id=p)
        r.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


