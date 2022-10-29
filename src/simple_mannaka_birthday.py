from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class SimpleBirthday:
    month: int
    day: int


class _Year(SimpleBirthday):
    def __init__(self, month: int, day: int, year: int):
        super().__init__(month, day)
        self._date = date(year, month, day)

    @staticmethod
    def _is_hayaumare(month: int) -> bool:
        return 1 <= month <= 3

    def __add__(self, other: timedelta) -> "_Year":
        added = self._date + other
        return _Year(added.month, added.day, added.year)


class _CommonYear(_Year):
    _THE_COMMON_YEAR = 2001

    def __init__(self, month: int, day: int):
        year = self._THE_COMMON_YEAR + self._is_hayaumare(month)
        super().__init__(month, day, year)

    def __sub__(self, other: "_CommonYear") -> timedelta:
        return self._date - other._date

    def __lt__(self, other: "_CommonYear") -> bool:
        return self._date < other._date


class _LeapYear(_Year):
    _LEAP_YEAR = 2000

    def __init__(self, month: int, day: int):
        year = self._LEAP_YEAR - 1 + self._is_hayaumare(month)
        super().__init__(month, day, year)

    def __sub__(self, other: "_LeapYear") -> timedelta:
        return self._date - other._date

    def __lt__(self, other: "_LeapYear") -> bool:
        return self._date < other._date

    @classmethod
    def is_leap(cls, birthday: SimpleBirthday) -> bool:
        return birthday.day == 29 and birthday.month == 2


class SimpleMannakaBirthday(SimpleBirthday):
    def __init__(self, birthday1: SimpleBirthday, birthday2: SimpleBirthday):
        mannaka_birthday = _simple_mannaka_birthday(birthday1, birthday2)
        super().__init__(mannaka_birthday.month, mannaka_birthday.day)
        self._birthdays = birthday1, birthday2
        self._mannaka_birthday = mannaka_birthday


def _simple_mannaka_birthday(
    birthday1: SimpleBirthday, birthday2: SimpleBirthday
) -> SimpleBirthday:
    birthdays = birthday1, birthday2

    if any(map(_LeapYear.is_leap, birthdays)):
        l_year1, l_year2 = sorted(_LeapYear(**b.__dict__) for b in birthdays)
        delta = l_year2 - l_year1
        return l_year1 + timedelta(delta.days / 2)
    else:
        c_year1, c_year2 = sorted(_CommonYear(**b.__dict__) for b in birthdays)
        delta = c_year2 - c_year1
        return c_year1 + timedelta(delta.days / 2)
