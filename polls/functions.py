from polls.models import Cookie, Comments
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth.models import User


def get_vote_form(request, cookies):
    result = []
    # list=[]
    for cookie in cookies:
        try:
            comments = Comments.objects.filter(cookie_id=cookie.pk)
        except(Exception):
            pass
        else:
            for comment in comments:
                user_name = User.objects.get(pk=comment.user_id.pk).username
                result.append([cookie.pk, user_name, comment.comment])


    # user = get_user(request)
    # try:
    #     cookies_id_list = Relations.objects.filter(user_id=user)
    # except(Exception):
    #     pass
    # else:
    #     for c in cookies_id_list:
    #         list.append(c.cookie_id.pk)

    return {'cookies': cookies, "result": result}
    # return {'cookies': cookies, "result": result, "votes_list": list}


# def get_votes(request):
#     user = get_user(request)
#     cookies_id_list = Relations.objects.filter(user_id=user.pk)
#     return cookies_id_list