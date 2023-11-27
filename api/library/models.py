from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from datetime import datetime
from . import validators, managers


class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self) -> str:
        return str(self)


class Book(models.Model):
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    objects = managers.BookManager()

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="books"
    )
    name = models.CharField("Название", max_length=255)
    issue_year = models.PositiveSmallIntegerField(
        "Год издания", validators=[MaxValueValidator(datetime.now().year)]
    )
    isbn = models.CharField(
        "ISBN", max_length=17, validators=[validators.ISBNValidator()]
    )

    @property
    def get_absolute_url(self) -> str:
        return reverse("library:book-detail", kwargs={"pk": self.pk})
