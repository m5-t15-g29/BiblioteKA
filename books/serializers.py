from rest_framework import serializers
from .models import Book, BooksUser, BooksLikes
from users.serializers import UserSerializer
from users.models import User


class BookSerializer(serializers.ModelSerializer):
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
            "users_follow",
            "likes_positive",
            "likes_negative",
        ]

    users_follow = serializers.SerializerMethodField()
    likes_positive = serializers.SerializerMethodField()
    likes_negative = serializers.SerializerMethodField()

    def get_users_follow(self, obj):
        try:
            users = Book.users.through.objects.filter(book__pk=obj.id)
            user_follow = []
            for user in users:
                item = User.objects.get(id=user.user_id)
                user_follow.append({"id": item.id, "name": item.name})
        except Book.DoesNotExist:
            return []
        return user_follow

    def get_likes_positive(self, obj):
        users = Book.likes.through.objects.filter(book__pk=obj.id)
        user_likes = 0
        for user in users:
            if user.user_liked:
                user_likes = user_likes + 1
        return user_likes

    def get_likes_negative(self, obj):
        users = Book.likes.through.objects.filter(book__pk=obj.id)
        user_likes = 0
        for user in users:
            if not user.user_liked:
                user_likes = user_likes + 1
        return user_likes


class BooksUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = BooksUser
        fields = ["id", "user", "book", "user_follow"]

        extra_kwargs = {"user_follow": {"required": False, "default": True}}


class BooksLikesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = BooksLikes
        fields = ["id", "user", "book", "user_liked"]

        extra_kwargs = {"user_liked": {"required": False, "default": False}}
