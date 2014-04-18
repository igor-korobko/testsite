# from django.contrib.comments.views.moderation import delete
from django.conf.global_settings import MEDIA_ROOT
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_delete
from django.core.files.storage import FileSystemStorage


class Cookie(models.Model):

    rating = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to="cookies")


def del_img(sender, **k):
    obj = k['instance']
    if obj.img != sender.objects.get(pk=obj.pk).img:
        f = FileSystemStorage()
        f.delete(MEDIA_ROOT + sender.objects.get(pk=obj.pk).img.__str__())


def del_img_with_post(sender, **k):
    obj = k['instance']
    f = FileSystemStorage()
    f.delete(MEDIA_ROOT + obj.img.__str__())


pre_save.connect(del_img, sender=Cookie)
post_delete.connect(del_img_with_post, sender=Cookie)


class Comments(models.Model):
    cookie_id = models.ForeignKey(Cookie)
    user_id = models.ForeignKey(User)
    comment = models.TextField()


class Relations(models.Model):
    user_id = models.ForeignKey(User)
    comment_id = models.ForeignKey(Comments)

