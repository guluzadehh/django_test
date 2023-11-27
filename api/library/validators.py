from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ISBNValidator:
    message = "Неверный формат ISBN"

    def __call__(self, value: str):
        self.value = value.replace("-", "")
        self.validate()

    def validate(self):
        self.validate_length()
        self.validate_sum()

    def validate_length(self):
        if not self.is_10_digit() and not self.is_13_digit():
            raise ValidationError(self.message)

    def validate_sum(self):
        if self.get_sum() % self.get_mod() != 0:
            raise ValidationError(self.message)

    def get_mod(self) -> int:
        if self.is_10_digit():
            return 11
        elif self.is_13_digit():
            return 10

    def get_sum(self) -> int:
        if self.is_10_digit():
            return self.get_10_digit_sum()
        elif self.is_13_digit():
            return self.get_13_digit_sum()

    def get_10_digit_sum(self) -> int:
        return sum((i + 1) * self.parse_digit(x) for i, x in enumerate(self.value))

    def get_13_digit_sum(self) -> int:
        return sum(
            (1 if i % 2 == 0 else 3) * self.parse_digit(x)
            for i, x in enumerate(self.value)
        )

    def is_10_digit(self) -> bool:
        return len(self.value) == 10

    def is_13_digit(self) -> bool:
        return len(self.value) == 13

    def parse_digit(self, digit: str) -> int:
        if digit.upper() == "X":
            return 10

        if not digit.isnumeric():
            raise ValidationError(self.message)

        return int(digit)
