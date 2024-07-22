from django.db import models
from django.contrib.auth.models import AbstractUser


class Reader(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    taken_by = models.ForeignKey(Reader, on_delete=models.SET_NULL, null=True)


class User(AbstractUser):
    username = models.CharField(max_length=100, primary_key=True, unique=True)
    user_types = (('A', 'admin'),
                  ('R', 'reader'))
    type_of_user = models.CharField(max_length=1, choices=user_types)
