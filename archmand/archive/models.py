# -*- coding=UTF-8 -*-

from django.db import models


class Archives(models.Model):
    archive = models.CharField(max_length=10)
    identity = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birthday = models.CharField(max_length=20)
    retire_date = models.CharField(max_length=20)
    female_cadre = models.BooleanField()
    special_personnel = models.BooleanField()
    transfer_out = models.CharField(max_length=100)

    class Meta:
        db_table = "archives"


class User(models.Model):
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    auth_ament = models.BooleanField()

    class Meta:
        db_table = 'users'
