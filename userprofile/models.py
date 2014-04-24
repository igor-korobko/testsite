from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_delete
from django.core.files.storage import FileSystemStorage
from django.conf.global_settings import MEDIA_ROOT


class MyUserModel(models.Model):
    user = models.OneToOneField(User)
    about = models.TextField()
    photo = models.ImageField(upload_to="photos")

User.profile = property(lambda u: MyUserModel.objects.get_or_create(user=u)[0])


def del_img(sender, **k):
    obj = k['instance']
    try:
        old_obj = sender.objects.get(pk=obj.pk)
    except(sender.DoesNotExist):
        pass
    else:
        if old_obj.photo:
            if obj.photo != old_obj.photo:
                f = FileSystemStorage()
                f.delete(MEDIA_ROOT + sender.objects.get(pk=obj.pk).photo.__str__())


def del_img_with_post(sender, **k):
    obj = k['instance']
    f = FileSystemStorage()
    f.delete(MEDIA_ROOT + obj.photo.__str__())

pre_save.connect(del_img, sender=MyUserModel)
post_delete.connect(del_img_with_post, sender=MyUserModel)