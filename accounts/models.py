from django.db import models

class Avatar(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    user_id = models.IntegerField(default=-1)