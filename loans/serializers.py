from rest_framework import serializers
from .models import Loan
from users.serializers import UserSerializer
from copies.serializers import CopieSerializer
from datetime import datetime
from copies.models import Copie


class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    copie = CopieSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = ("id", "create_at", "return_date", "returned_date", "copie", "user")
        read_only_fields = [
            "create_at",
            "return_date",
            "returned_date",
        ]

    def create(self, validated_data):
        user = validated_data.pop("user")
        copie = validated_data.pop("copie")

        copie.is_loaned = True
        copie.save()

        now = datetime.now()
        return_date = datetime(now.year, now.month, (now.day + 2))
        if return_date.strftime("%w") == 6:
            return_date = datetime(now.year, now.month, (now.day + 3))
        elif return_date.strftime("%w") == 2:
            return_date = datetime(now.year, now.month, (now.day + 4))

        validated_data["return_date"] = return_date

        return Loan.objects.create(**validated_data, user=user, copie=copie)

    def update(self, instance: Loan, validated_data: dict):
        validated_data["returned_date"] = datetime.now()

        copie = Copie.objects.get(id=instance.copie_id)
        copie.is_loaned = False
        copie.save()
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
