from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_delete
from signals import *


class MyUserModel(models.Model):
    user = models.OneToOneField(User)
    about = models.TextField()
    photo = models.ImageField(upload_to="photos")

User.profile = property(lambda u: MyUserModel.objects.get_or_create(user=u)[0])

pre_save.connect(del_img, sender=MyUserModel)
post_delete.connect(del_img_with_post, sender=MyUserModel)