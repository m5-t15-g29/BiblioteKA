from rest_framework import serializers
from books.serializers import BookSerializer
from books.models import Book
from .models import Copie


class CopieSerializer(serializers.ModelSerializer):
    is_loaned = serializers.BooleanField(default=False)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Copie
        fields = ("id", "is_loaned", "book")

        # reduzir as informações de retorno do book na copia
