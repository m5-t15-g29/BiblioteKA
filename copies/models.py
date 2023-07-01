from django.db import models


class Copie(models.Model):
    quantity = models.PositiveIntegerField()

    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )
