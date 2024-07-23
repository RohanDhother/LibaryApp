from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Reader
from .serializer import BookSerializer, ReaderSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
