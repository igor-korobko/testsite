from polls.models import Cookie, Comments
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth.models import User


def get_comments(request, cookies):
    result = []
    for cookie in cookies:
        comments = Comments.objects.filter(cookie_id=cookie.pk)
        for comment in comments:
            user_name = User.objects.get(pk=comment.user_id.pk).username
            result.append([cookie.pk, user_name, comment.comment])
    return {'cookies': cookies, "result": result}