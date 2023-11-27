from django.test import TestCase
from library import factories


class AuthorModelTestCase(TestCase):
    def setUp(self) -> None:
        self.author = factories.AuthorFactory()

    def test_full_name(self):
        self.assertEqual(
            self.author.full_name, f"{self.author.first_name} {self.author.last_name}"
        )


class BookModelTestCase(TestCase):
    def setUp(self) -> None:
        self.book = factories.BookFactory()

    def test_get_absolute_url(self):
        self.assertEqual(self.book.get_absolute_url, f"/api/books/{self.book.pk}/")
