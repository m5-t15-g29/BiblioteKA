from django.db import models


class Loan(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True)
    copie = models.ForeignKey(
        "copies.Copie", on_delete=models.CASCADE, related_name="loans"
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loans"
    )
