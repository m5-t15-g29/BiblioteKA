from rest_framework import serializers
from .models import Book, BooksUser
from users.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Book

        fields = [
            "id",
            "name",
            "status",
            "author",
            "sinopse",
            "publisher",
            "quantity",
            "created_at",
            "user",
        ]


class BooksUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksUser
        fields = ["id", "user", "book", "user_liked", "user_follow", "user_comment"]

        extra_kwargs = {
            "user_liked": {"required": False, "default": False},
            "user_follow": {"required": False, "default": False},
            "user_comment": {"required": False},
        }
