from django.contrib import admin


from mptt.admin import MPTTModelAdmin


from .models import treeItem, folder, fileNote
# Register your models here.

admin.site.register(treeItem)
admin.site.register(folder)
admin.site.register(fileNote)
