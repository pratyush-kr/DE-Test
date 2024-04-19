from django.db import models


# Create your models here.

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=2000)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)


class GPTResponseData(models.Model):
    response_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=8192)
    create_date = models.DateField(auto_now_add=True)
    create_time = models.TimeField(auto_now_add=True)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    create_date = models.DateField(auto_now_add=True)
    create_time = models.TimeField(auto_now_add=True)


class Demo(models.Model):
    demo_id = models.AutoField(primary_key=True)
    data = models.CharField(max_length=2000)
