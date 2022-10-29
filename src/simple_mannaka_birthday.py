from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class Birthday:
    month: int
    day: int


def mannaka_birthday(birthday1: Birthday, birthday2: Birthday) -> Birthday:
    NON_INTERCALARY_YEAR = 2001

    def calib_date(birthday: Birthday) -> date:
        is_hayaumare = 1 <= birthday.month <= 3
        return date(NON_INTERCALARY_YEAR + is_hayaumare, **birthday.__dict__)

    date1, date2 = sorted(map(calib_date, (birthday1, birthday2)))
    delta = date2 - date1
    mannaka = date1 + timedelta(delta.days / 2)
    return Birthday(mannaka.month, mannaka.day)
