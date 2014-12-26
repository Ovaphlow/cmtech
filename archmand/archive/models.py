# -*- coding=UTF-8 -*-

from django.db import models


class Archive(models.Model):
    archive = models.CharField(max_length=10)
    identity = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, default=u'男')
    birthday = models.CharField(max_length=20)
    retire_date = models.CharField(max_length=20)
    female_cadre = models.BooleanField(default=0)
    special_personnel = models.BooleanField(default=0)
    transfer_out = models.CharField(max_length=100)

    class Meta:
        db_table = "archive"
