from rest_framework import serializers
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
            "user",
        ]

    def updated(self, instance: Book, validated_data: dict) -> Book:
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
    class Meta:
        model = BooksUser
        fields = ["id", "user", "book", "user_follow"]

        extra_kwargs = {"user_follow": {"required": False, "default": False}}


class BooksLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLikes
        fields = ["id", "user", "book", "user_liked"]

        extra_kwargs = {"user_liked": {"required": False, "default": False}}
