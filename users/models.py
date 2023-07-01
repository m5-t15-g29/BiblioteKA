from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    is_student = models.BooleanField()
    is_employee = models.BooleanField(default=False)
    is_loan_blocked = models.BooleanField(default=False)
