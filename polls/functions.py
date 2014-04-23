from polls.models import Cookie, Comments, Relations
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth.models import User


def get_vote_form(request, cookies):
    result = []
    for cookie in cookies:
        comments = Comments.objects.filter(cookie_id=cookie.pk)
        for comment in comments:
            user_name = User.objects.get(pk=comment.user_id.pk).username
            result.append([cookie.pk, user_name, comment.comment])

    user = get_user(request)
    cookies_id_list = Relations.objects.filter(user_id=user.id)

    return {'cookies': cookies, "result": result, "cookies_id_list": cookies_id_list}


# def get_votes(request):
#     user = get_user(request)
#     cookies_id_list = Relations.objects.filter(user_id=user.pk)
#     return cookies_id_list