from dataclasses import dataclass
from datetime import date, timedelta

from simple_mannaka_birthday import SimpleBirthday, BirthdayBase


@dataclass
class Birthday(BirthdayBase, SimpleBirthday):
    _CALIB = timedelta(1)
    _year: int

    def to_date(self) -> date:
        return self._calibed_next_date() - self._CALIB

    def next(self) -> "Birthday":
        return Birthday(self.month, self.day, self._year + 1)

    def prev(self) -> "Birthday":
        return Birthday(self.month, self.day, self._year - 1)

    def _is_intercalary(self) -> bool:
        return self.day == 29 and self.month == 2

    def _calibed_next_date(self) -> date:
        if self._is_intercalary():
            return date(self._year, 3, 1)
        return date(self._year, self.month, self.day) + self._CALIB


class MannakaBirthday(BirthdayBase):
    def __init__(self, birthday1: BirthdayBase, birthday2: BirthdayBase):
        self._birthdays = (birthday1, birthday2)

        assert (date1 := birthday1.to_date()) and (date2 := birthday2.to_date())
        assert 0 <= (date2 - date1).days <= 366 * 2

    def to_date(self) -> date:
        date1, date2 = (b.to_date() for b in self._birthdays)

        delta = date2 - date1

        return date1 + timedelta(delta.days / 2)

    def next(self, target: date | None = None) -> "MannakaBirthday":
        if target is None:
            return self._next_base()

        m = self

        delta_days = (m.to_date() - target).days

        if delta_days == 0:
            return m

        if delta_days > 0:
            m_next = m
            for _ in range(abs(delta_days)):
                if m.to_date() < target:
                    return m_next
                m_next = m
                m = m._prev_base()

        if delta_days < 0:
            for _ in range(abs(delta_days)):
                if m.to_date() > target:
                    return m
                m = m._next_base()

        raise Exception()

    def prev(self, target: date | None = None) -> "MannakaBirthday":
        if target is None:
            return self._prev_base()

        return self.next(target)._prev_base()

    def _next_base(self) -> "MannakaBirthday":
        b1, b2 = self._birthdays
        return MannakaBirthday(b2, b1.next())

    def _prev_base(self) -> "MannakaBirthday":
        b1, b2 = self._birthdays
        return MannakaBirthday(b2.prev(), b1)
