from django.db import models
from django.utils import timezone

class Contact(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  subject = models.CharField(max_length=200)
  message = models.TextField(blank=True)
  author = models.IntegerField(default=-1, blank=True)
  author_name = models.CharField(max_length=200, blank=True)
  target = models.IntegerField(default=-1)
  target_name = models.CharField(max_length=200, blank=True)
  contact_date = models.DateTimeField(default=timezone.now, blank=True)
  def __str__(self):
    return self.name