from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class Cookie(models.Model):
    rating = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to="polls/static/polls/img")


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