import factory
from faker import Faker
from . import models

faker: Faker = Faker("ru-RU")


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Author

    first_name = faker.first_name()
    last_name = faker.last_name()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Book

    author = factory.SubFactory(AuthorFactory)
    name = faker.text(max_nb_chars=255)
    issue_year = faker.year()
    isbn = faker.isbn10()
