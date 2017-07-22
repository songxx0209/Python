from __future__ import unicode_literals

from django.db import models

# Create your models here
class Articles(models.Model):
    title=models.CharField(max_length=100, default='Title')
    content=models.TextField(null=True)
