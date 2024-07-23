from django.db import models


class Reader(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    taken_by = models.ForeignKey(Reader, on_delete=models.SET_NULL, null=True, blank=True)
