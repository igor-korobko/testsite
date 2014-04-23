from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class MyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'identifier'
# Create your models here.
