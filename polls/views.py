# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from polls.models import Cookie
from django.contrib.auth import authenticate, login


def index(request):
    cookies = Cookie.objects.all()
    return render(request, "polls/index.html", {'cookies': cookies})


def search(request):
    try:
        cookies = Cookie.objects.filter(name=request.POST['search'])
        return render(request, "polls/index.html", {'cookies': cookies})
    except(Exception):
        return HttpResponseRedirect(reverse('polls:index'))


def login_(request):

    try:
        log = request.POST['login']
        pwd = request.POST['pwd']
        user = authenticate(username=log, password=pwd)
        cookies = Cookie.objects.all()
        message = ""
        if user is not None:
            if user.is_active:
                login(request, user)
        else:
            message = "Не верный логин или пароль"

        return render(request, "polls/index.html", {"cookies": cookies, "msg": message})

    except(Exception):
        return HttpResponseRedirect(reverse('polls:index'))


def vote(request):
    p = get_object_or_404(Cookie, pk=request.POST['cookie_id'])
    p.rating += int(request.POST['choice'])
    p.save()
    return HttpResponseRedirect(reverse('polls:index'))








# from polls.models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/detail.html', context)
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#
#