from django.contrib import admin

from .models import accounts, positions

# Register your models here.

admin.site.register(accounts)
admin.site.register(positions)