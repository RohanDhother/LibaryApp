from rest_framework import serializers
from .models import Book, Reader


class BookSerializer(serializers.ModelSerializer):
    taken_by = serializers.SlugRelatedField(
        queryset=Reader.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Book
        fields = '__all__'


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'
