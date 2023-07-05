# Generated by Django 4.2.2 on 2023-07-05 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookslikes',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
        migrations.AddField(
            model_name='bookslikes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(related_name='books_liked', through='books.booksLikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(related_name='books_follow', through='books.BooksUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
