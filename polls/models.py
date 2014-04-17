# from django.contrib.comments.views.moderation import delete
from django.conf.global_settings import MEDIA_ROOT
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
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



pre_save.connect(del_img, sender=Cookie)



class Comments(models.Model):
    cookie_id = models.ForeignKey(Cookie)
    user_id = models.ForeignKey(User)
    comment = models.TextField()


class Relations(models.Model):
    user_id = models.ForeignKey(User)
    comment_id = models.ForeignKey(Comments)

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date < now
#
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
#
#     def __str__(self):
#         return self.question_text
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)