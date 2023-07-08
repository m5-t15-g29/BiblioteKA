from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from books.models import Book
from django.forms.models import model_to_dict


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "name",
            "email",
            "password",
            "is_loan_blocked",
            "is_superuser",
            "books_liked",
            "books_follow",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"required": False, "default": False},
        }
        read_only_filds = ["is_loan_blocked"]

    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="This field must be unique."
            )
        ],
    )

    books_liked = serializers.SerializerMethodField()
    books_follow = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> User:
        if validated_data["is_superuser"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def updated(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(raw_password=instance.password)

        instance.save()

        return instance


    def get_books_liked(self, obj):
        books = User.books_liked.through.objects.filter(user__pk=obj.id)
        books_liked = []
        for book in books:
            item = Book.objects.get(id=book.book_id)
            books_liked.append(
                {"id": item.id, "name": item.name, "like_status": book.user_liked}
            )
        return books_liked

    def get_books_follow(self, obj):
        books = User.books_follow.through.objects.filter(user__pk=obj.id)
        books_follow = []
        for book in books:
            item = Book.objects.get(id=book.book_id)
            books_follow.append(
                {"id": item.id, "name": item.name, "status": item.status}
            )
        return books_follow
