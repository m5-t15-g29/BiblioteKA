from django.db import models
from users.models import User


class Book(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    author = models.CharField(max_length=50)
    sinopse = models.TextField()
    publisher = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    users = models.ManyToManyField(
        "users.User",
        through="BooksUser",
        related_name="books_follow",
    )

    likes = models.ManyToManyField(
        "users.User", through="BooksLikes", related_name="books_liked"
    )


class booksLikes(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_liked = models.BooleanField(default=False)


class BooksUser(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_follow = models.BooleanField(default=False)
