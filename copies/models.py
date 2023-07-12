from django.db import models


class Copie(models.Model):
    is_loaned = models.BooleanField(default=False)

    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )
