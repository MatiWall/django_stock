from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


from mptt.models import MPTTModel, TreeForeignKey

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





class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']





# File structure

class treeItem(MPTTModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = TreeForeignKey('self', null = True, blank = True, related_name = 'children', on_delete=models.CASCADE)
    
    


class folder(models.Model):
    name = models.CharField(max_length = 50)
    folder = GenericRelation(treeItem)

    def __str__(self):
        return self.name


class fileNote(models.Model):
    fileName = models.CharField(max_length = 255)
    dataCreated = models.DateTimeField(auto_now_add = True)
    dateUpdated = models.DateTimeField(auto_now = True)