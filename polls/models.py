from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_delete
from signals import *


class Cookie(models.Model):

    rating = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to="cookies")
    user = models.ManyToManyField(User)

pre_save.connect(del_img, sender=Cookie)
post_delete.connect(del_img_with_post, sender=Cookie)


class Comments(models.Model):
    cookie_id = models.ForeignKey(Cookie)
    user_id = models.ForeignKey(User)
    comment = models.TextField()



