from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Book, BooksUser, BooksLikes
from users.models import User
from users.serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings


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
            "likes",
            "dislikes",
        ]

        read_only_fields = ["quantity"]

        name = serializers.CharField(
            validators=[
                UniqueValidator(
                    queryset=Book.objects.all(),
                    message="A book with this name has already been created",
                )
            ],
        )

    users_follow = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()

    def get_users_follow(self, obj):
        try:
            users = Book.users.through.objects.filter(book__pk=obj.id)
            user_follow = []
            for user in users:
                item = User.objects.get(id=user.user_id)
                user_follow.append(
                    {"id": item.id, "name": item.name, "email": item.email}
                )
        except Book.DoesNotExist:
            return []
        return user_follow

    def get_likes(self, obj):
        users = Book.likes.through.objects.filter(book__pk=obj.id)
        user_likes = 0
        for user in users:
            if user.user_liked:
                user_likes = user_likes + 1
        return user_likes

    def get_dislikes(self, obj):
        users = Book.likes.through.objects.filter(book__pk=obj.id)
        user_likes = 0
        for user in users:
            if not user.user_liked:
                user_likes = user_likes + 1
        return user_likes

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if instance.status:
            for user in instance.users_follow:
                send_mail(
                    subject="status do livro seguido",
                    message=f"o livro {instance.name} está aberto para empréstimo",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=user.email,
                )
        instance.save()

        return instance


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
