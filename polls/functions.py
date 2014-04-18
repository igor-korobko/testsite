from models import Comments

from django.contrib.auth import get_user


def get_cookie_comment(cookie_list, user_id):
    result = []
    for cookie in cookie_list:
        result.append(cookie.pk)
        comments = Comments.objects.get(cookie_id=cookie.pk, user_id=user_id)
        for comment in comments:
            result[cookie.pk].append([user_id,comment])