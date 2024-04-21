from datetime import timedelta

from rest_framework.validators import ValidationError


class NiceOrHelpfulValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        is_nice = value.get(self.fields[0])
        prise = value.get(self.fields[1])
        if is_nice and prise:
            raise ValidationError("Нельзя одновременно указывать приятную привычку и вознаграждение!")


class DurationValidator:
    max_duration = 120

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        duration = value.get(self.fields[0])
        if duration and duration > timedelta(seconds=self.max_duration):
            raise ValidationError("Привычка не должна быть дольше 120 секунд")


class ChainIsNiceValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        chain_nice = value.get(self.fields[0])
        if chain_nice:
            if not chain_nice.is_nice:
                raise ValidationError("Привычка-вознаграждение должна быть приятной")


class NiceWithoutPriseOrNice:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        if value.get(self.fields[0]) or value.get(self.fields[1]):
            raise ValidationError("Привычка-вознаграждение не может иметь приятных последствий")


class PeriodValidator:
    max_period = 7

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        period = value.get(self.fields[0])
        if period and period > self.max_period:
            raise ValidationError("Привычка не должна быть реже чем раз в 7 дней")
