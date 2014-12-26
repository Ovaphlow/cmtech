# -*- coding=UTF-8 -*-

from django.db import models


class User(models.Model):
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    auth_ament = models.BooleanField(default=0)

    class Meta:
        db_table = 'user'
