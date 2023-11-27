from unittest import TestCase
from django.core.exceptions import ValidationError
from .. import validators


class ISBNValidatorTestCase(TestCase):
    def setUp(self):
        self.validator = validators.ISBNValidator()

    def test_invalid_size(self):
        LESS_SIZED_ISBN = "24-54"
        HIGH_SIZED_ISBN = "0-306-40615-1245-25124"
        self.assertRaises(ValidationError, self.validator, LESS_SIZED_ISBN)
        self.assertRaises(ValidationError, self.validator, HIGH_SIZED_ISBN)

    def test_valid_isbn_10(self):
        VALID_ISBN_10 = "0-15-781565-X"
        self.assertIsNone(self.validator(VALID_ISBN_10))

    def test_invalid_isbn_10(self):
        INVALID_ISBN_10 = "0-306-40615-1"
        self.assertRaises(ValidationError, self.validator, INVALID_ISBN_10)

    def test_valid_isbn_13(self):
        VALID_ISBN_13 = "978-0-306-40615-7"
        self.assertIsNone(self.validator(VALID_ISBN_13))

    def test_valid_isbn_13(self):
        INVALID_ISBN_13 = "978-0-306-40615-6"
        self.assertRaises(ValidationError, self.validator, INVALID_ISBN_13)
