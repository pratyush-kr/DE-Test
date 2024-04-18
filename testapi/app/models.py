from django.db import models


# Create your models here.

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=2000)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
