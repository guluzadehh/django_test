from django.db.models import Manager
from django.db.models.query import QuerySet


class BookManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().select_related("author")
