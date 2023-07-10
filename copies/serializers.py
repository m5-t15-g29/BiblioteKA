from rest_framework import serializers
from books.serializers import BookSerializer
from books.models import Book
from .models import Copie


class CopieSerializer(serializers.ModelSerializer):
    is_loaned = serializers.BooleanField(default=False, read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Copie
        fields = ("id", "is_loaned", "book")

    def create(self, validated_data):
        book_filtered = validated_data.pop("book")
        book_filtered.quantity = book_filtered.quantity + 1
        book_filtered.status = True
        book_filtered.save()
        return Copie.objects.create(**validated_data, book=book_filtered)

    def update(self, instance, validated_data):
        book = Book.objects.get(id=instance.book_id)
        if validated_data["is_loaned"]:
            book.quantity = book.quantity - 1
        else:
            book.quantity = book.quantity + 1
        if book.quantity == 0:
            book.status = False
        else:
            book.status = True
        book.save()
        return super().update(instance, validated_data)
