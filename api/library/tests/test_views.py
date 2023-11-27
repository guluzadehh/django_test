from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from library.factories import BookFactory, AuthorFactory
from library.models import Book
from datetime import datetime


class BookListCreateAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.BOOKS_SIZE = 5
        self.books: list[Book] = BookFactory.create_batch(self.BOOKS_SIZE)

    def test_list_books(self):
        res = self.client.get(reverse("library:book-list"))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), self.BOOKS_SIZE)

    def test_create_book(self):
        new_book: Book = BookFactory.build(author=AuthorFactory())
        res = self.client.post(
            reverse("library:book-list"),
            {
                "name": new_book.name,
                "author": new_book.author.id,
                "issue_year": new_book.issue_year,
                "isbn": new_book.isbn,
            },
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), self.BOOKS_SIZE + 1)

    def test_create_book_empty_name(self):
        new_book: Book = BookFactory.build(author=AuthorFactory())
        res = self.client.post(
            reverse("library:book-list"),
            {
                "name": "",
                "author": new_book.author.id,
                "issue_year": new_book.issue_year,
                "isbn": new_book.isbn,
            },
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.all().count(), self.BOOKS_SIZE)

    def test_create_book_empty_author(self):
        new_book: Book = BookFactory.build(author=AuthorFactory())
        res = self.client.post(
            reverse("library:book-list"),
            {
                "name": new_book.name,
                "author": "",
                "issue_year": new_book.issue_year,
                "isbn": new_book.isbn,
            },
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.all().count(), self.BOOKS_SIZE)

    def test_create_book_empty_issue_year(self):
        new_book: Book = BookFactory.build(author=AuthorFactory())
        res = self.client.post(
            reverse("library:book-list"),
            {
                "name": new_book.name,
                "author": new_book.author.id,
                "issue_year": "",
                "isbn": new_book.isbn,
            },
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.all().count(), self.BOOKS_SIZE)

    def test_create_book_wrong_issue_year(self):
        new_book: Book = BookFactory.build(author=AuthorFactory())
        res = self.client.post(
            reverse("library:book-list"),
            {
                "name": new_book.name,
                "author": new_book.author.id,
                "issue_year": datetime.now().year + 1,
                "isbn": new_book.isbn,
            },
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.all().count(), self.BOOKS_SIZE)

    def test_create_book_empty_isbn(self):
        new_book: Book = BookFactory.build(author=AuthorFactory())
        res = self.client.post(
            reverse("library:book-list"),
            {
                "name": new_book.name,
                "author": new_book.author.id,
                "issue_year": new_book.issue_year,
                "isbn": "",
            },
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.all().count(), self.BOOKS_SIZE)

    def test_create_book_wrong_isbn(self):
        new_book: Book = BookFactory.build(author=AuthorFactory())
        res = self.client.post(
            reverse("library:book-list"),
            {
                "name": new_book.name,
                "author": new_book.author.id,
                "issue_year": new_book.issue_year,
                "isbn": "1234567890",
            },
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Book.objects.all().count(), self.BOOKS_SIZE)
