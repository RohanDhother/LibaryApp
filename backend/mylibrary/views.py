from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book, Reader
from .serializer import (BookSerializer,
                         ReaderSerializer,
                         ReaderNameSerializer,
                         BookUpdateSerializer)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def partial_update(self, request, *args, **kwargs):
        serializer = BookUpdateSerializer(instance=self.get_object(),
                                          data=request.data,
                                          partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(True)


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderNameViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderNameSerializer
