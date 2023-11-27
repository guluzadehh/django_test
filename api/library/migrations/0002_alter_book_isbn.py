# Generated by Django 4.2.7 on 2023-11-23 23:42

from django.db import migrations, models
import library.validators


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.TextField(
                validators=[library.validators.ISBNValidator()], verbose_name="ISBN"
            ),
        ),
    ]
