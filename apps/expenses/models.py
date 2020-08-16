from django.db import models
from django.shortcuts import reverse

from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length  = 255)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name


class Expense(models.Model):

    amount = models.FloatField()
    date = models.DateField( default= now)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.category

    class Meta:
        ordering: ['-date']







class IncomeSource(models.Model):
    name = models.CharField(max_length = 255)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Income(models.Model):
    amount = models.FloatField()
    date = models.DateField(default = now)
    description = models.TextField()
    source = models.ForeignKey(IncomeSource, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.source

    class Meta:
        ordering: ['-date']



