from django.contrib import admin
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display: list[str] = ["full_name"]


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display: list[str] = ["name", "author", "isbn"]
