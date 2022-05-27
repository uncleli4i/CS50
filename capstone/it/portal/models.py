from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    pass


# Models for Computers Inventory

class Monitor(models.Model):
    model = models.CharField(max_length=50)
    diag = models.IntegerField()
    def __str__(self):
        return self.model


class OS(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class HDD(models.Model):
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    capacity = models.IntegerField()
    def __str__(self):
        return self.model

class RAM(models.Model):
    model = models.CharField(max_length=100)
    capacity = models.IntegerField()
    def __str__(self):
        return self.model


class CPU(models.Model):
    model = models.CharField(max_length=100)
    def __str__(self):
        return self.model


class Comps(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CPU = models.ForeignKey(CPU, on_delete=models.CASCADE)
    RAM = models.ForeignKey(RAM, on_delete=models.CASCADE)
    HDD = models.ForeignKey(HDD, on_delete=models.CASCADE)
    OS = models.ForeignKey(OS, on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    installed = models.DateField(default= datetime.now)
    def __str__(self):
        return self.name

