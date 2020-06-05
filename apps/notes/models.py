from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.


class task(models.Model):
    title = models.CharField(max_length = 255)
    created = models.DateTimeField(auto_now_add = True)
    compelted = models.BooleanField(default = False)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title  

class stickyNote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    notes = JSONField()

