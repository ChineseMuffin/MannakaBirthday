from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class SimpleBirthday:
    month: int
    day: int


class SimpleMannakaBirthday(SimpleBirthday):
    def __init__(self, birthday1: SimpleBirthday, birthday2: SimpleBirthday):
        mannaka_birthday = _simple_mannaka_birthday(birthday1, birthday2)
        super().__init__(**mannaka_birthday.__dict__)
        self._birthdays = birthday1, birthday2
        self._mannaka_birthday = mannaka_birthday


def _simple_mannaka_birthday(
    birthday1: SimpleBirthday, birthday2: SimpleBirthday
) -> SimpleBirthday:
    date1, date2 = sorted(_Leap.calibed_date(birthday1, birthday2))
    delta = date2 - date1
    mannaka = date1 + timedelta(delta.days / 2)
    return SimpleBirthday(mannaka.month, mannaka.day)


class _Leap:
    _LEAP_YEAR = 2000  # the next year is commmon
    _THE_COMMON_YEAR = 2001  # the next year is also common

    @classmethod
    def calibed_date(
        cls, birthday1: SimpleBirthday, birthday2: SimpleBirthday
    ) -> tuple[date, date]:
        has_leap = any(map(cls._is_leap, (birthday1, birthday2)))
        year = cls._LEAP_YEAR if has_leap else cls._THE_COMMON_YEAR

        def calib_year(birthday: SimpleBirthday) -> date:
            is_hayaumare = 1 <= birthday.month <= 3
            return date(year + (not is_hayaumare), birthday.month, birthday.day)

        return calib_year(birthday1), calib_year(birthday2)

    @classmethod
    def _is_leap(cls, birthday: SimpleBirthday) -> bool:
        return birthday.day == 29 and birthday.month == 2
