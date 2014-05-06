from django.conf.global_settings import LANGUAGE_COOKIE_NAME
from polls.forms import VoteForm, CommentForm
from polls.models import Cookie, Comments
from django.contrib.auth.models import User
from userprofile.forms import LoginForm
from django.utils import translation
from django.views.i18n import set_language


def translate(request):
    if "language" in request.POST:
        translation.activate(request.POST["language"])
        set_language(request)


def get_all_forms(request, cookies):

    translate(request)

    result = []
    all_forms = {"cookies": cookies}
    all_forms.update({"voteForm": VoteForm()})
    all_forms.update({"commentForm": CommentForm()})
    all_forms.update({"form": LoginForm()})
    
    for cookie in cookies:
        try:
            comments = Comments.objects.filter(cookie_id=cookie.pk)
        except(Exception):
            pass
        else:
            for comment in comments:
                user_name = User.objects.get(pk=comment.user_id.pk).username
                result.append([cookie.pk, user_name, comment.comment])

    all_forms.update({"result": result})
    return all_forms

