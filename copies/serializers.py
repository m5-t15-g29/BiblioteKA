from rest_framework import serializers

from books.models import Book
from .models import Copie


class CopieSerializer(serializers.ModelSerializer):
    is_loaned = serializers.BooleanField(default=False)
    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source="book.title"
    )

    class Meta:
        model = Copie
        fields = ("is_loaned", "book")

    def create(self, validated_data):
        book_data = validated_data.pop("book")
        book = Book.objects.get(title=book_data)
        copie = Copie.objects.create(book=book, **validated_data)
        return copie
