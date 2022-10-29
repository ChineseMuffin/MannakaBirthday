from dataclasses import dataclass
from datetime import date, timedelta


class BirthdayBase:
    def to_date(self) -> date:
        raise NotImplementedError()

    def next(self) -> "BirthdayBase":
        raise NotImplementedError()

    def prev(self) -> "BirthdayBase":
        raise NotImplementedError()


@dataclass
class SimpleBirthday:
    month: int
    day: int


class SimpleMannakaBirthday(BirthdayBase):
    def __init__(self, birthday1: SimpleBirthday, birthday2: SimpleBirthday, year: int):
        self._birthdays = birthday1, birthday2
        self._year = year

    def to_date(self) -> date:
        mb = simple_mannaka_birthday(*self._birthdays)
        return date(self._year, mb.month, mb.day)

    def next(self) -> "SimpleMannakaBirthday":
        return SimpleMannakaBirthday(*self._birthdays, self._year + 1)

    def prev(self) -> "SimpleMannakaBirthday":
        return SimpleMannakaBirthday(*self._birthdays, self._year - 1)


def simple_mannaka_birthday(
    birthday1: SimpleBirthday, birthday2: SimpleBirthday
) -> SimpleBirthday:
    date1, date2 = sorted(map(_calib_date, (birthday1, birthday2)))
    delta = date2 - date1
    mannaka = date1 + timedelta(delta.days / 2)
    return SimpleBirthday(mannaka.month, mannaka.day)


def _calib_date(birthday: SimpleBirthday) -> date:
    _NON_LEAP_YEAR = 2001  # the next year is also not a leap year
    is_hayaumare = 1 <= birthday.month <= 3
    return date(_NON_LEAP_YEAR + is_hayaumare, birthday.month, birthday.day)
