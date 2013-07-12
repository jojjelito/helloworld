from django.db import models

class conlog(models.Model):
    who = models.CharField(max_length=200)
    when = models.DateTimeField('date published')
