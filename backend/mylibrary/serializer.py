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


class BookUpdateSerializer(serializers.ModelSerializer):
    reader_id = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ['id', 'reader_id', 'loan_start_date']

    def update(self, instance, validated_data):
        reader_id = validated_data.pop('reader_id')
        loan_start_date = validated_data.pop('loan_start_date')
        reader = Reader.objects.get(id=reader_id)
        instance.taken_by = reader
        instance.loan_start_date = loan_start_date
        instance.save()
        return instance


class ReaderSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()
    books = serializers.SerializerMethodField()

    class Meta:
        model = Reader
        fields = '__all__'

    def get_books_count(self, obj):
        return obj.book_set.count()

    def get_books(self, obj):
        books = obj.book_set.all()
        return BookSerializer(books, many=True).data


class ReaderNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['name', 'id']
