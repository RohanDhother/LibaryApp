from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializer import BookSerializer
from django.views.decorators.csrf import csrf_exempt


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
