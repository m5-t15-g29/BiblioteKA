# Generated by Django 4.2.2 on 2023-07-08 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_quantity_alter_booksuser_user_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
