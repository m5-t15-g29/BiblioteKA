from rest_framework import serializers
from .models import Book, BooksUser, BooksLikes
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
        fields = ["id", "user", "book", "user_follow"]

        extra_kwargs = {"user_follow": {"required": False, "default": False}}


class BooksLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLikes
        fields = ["id", "user", "book", "user_liked"]

        extra_kwargs = {"user_liked": {"required": False, "default": False}}
