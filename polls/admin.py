from django.contrib import admin
from polls.models import Cookie, Comments
from userprofile.models import MyUserModel
# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.http import request

class CookieAdmin(admin.ModelAdmin):
        fields = ('name', 'description', 'img')
        list_display = ('name', 'description', 'img')
        search_fields = ['name']


class CommentsAdmin(admin.ModelAdmin):
        fields = ('cookie_id', 'user_id', 'comment')
        list_display = ('cookie_id', 'user_id', 'comment')
        search_fields = ['comment']


# class RelationsAdmin(admin.ModelAdmin):
#         fields = ('cookie_id', 'user_id')
#         list_display = ('cookie_id', 'user_id')


class UserAdmin(admin.ModelAdmin):
    model = [User, MyUserModel]
    # list_display = ("username", "email")

class AdminProfile(admin.ModelAdmin):
    list = [UserAdmin]
    # model = User
    # list_display = ("about", "photo")

admin.site.register(Cookie, CookieAdmin)
admin.site.register(Comments, CommentsAdmin)
# admin.site.register(Relations, RelationsAdmin)
admin.site.register(MyUserModel, AdminProfile)


# from polls.models import Question, Choice


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_filter = ['pub_date']
#     search_fields = ['question_text']
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#
# admin.site.register(Question, QuestionAdmin)


# admin.site.register(Choice, ChoiceInline)
# Register your models here.