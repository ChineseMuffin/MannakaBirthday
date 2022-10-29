from dataclasses import dataclass
from datetime import date, timedelta

from simple_mannaka_birthday import (
    Birthday as SimpleBirthday,
    mannaka_birthday as simple_mannaka_birthday,
)


@dataclass
class Birthday(SimpleBirthday):
    CALIB = timedelta(1)
    year: int

    def to_date(self) -> date:
        return self._calibed_next_date() - self.CALIB

    def _is_intercalary(self) -> bool:
        return self.day == 29 and self.month == 2

    def _calibed_next_date(self) -> date:
        if self._is_intercalary():
            return date(self.year, 3, 1)
        return date(**self.__dict__) + self.CALIB


class MannakaBirthday:
    def __init__(self, birthday1: Birthday, birthday2: Birthday):

        self._birthdays = (birthday1, birthday2)

        date1, date2 = (b.to_date() for b in self._birthdays)
        assert 0 <= (date2 - date1).days <= 366 * 2

    def to_date(self) -> date:
        date1, date2 = (b.to_date() for b in self._birthdays)

        delta = date2 - date1
        mannaka = date1 + timedelta(delta.days / 2)

        return mannaka

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
                m = m._previous_base()

        if delta_days < 0:
            for _ in range(abs(delta_days)):
                if m.to_date() > target:
                    return m
                m = m._next_base()

        raise Exception()

    def previous(self, target: date | None = None) -> "MannakaBirthday":
        if target is None:
            return self._previous_base()

        return self.next(target)._previous_base()

    def _next_base(self) -> "MannakaBirthday":
        b1, b2 = self._birthdays
        return MannakaBirthday(b2, Birthday(b1.month, b1.day, b1.year + 1))

    def _previous_base(self) -> "MannakaBirthday":
        b1, b2 = self._birthdays
        return MannakaBirthday(Birthday(b2.month, b2.day, b2.year - 1), b1)


class SimpleMannakaBirthday:
    def __init__(self, birthday1: Birthday, birthday2: Birthday):
        self._year1 = birthday1.year
        self._birthdays = birthday1, birthday2

    def to_date(self) -> date:
        mb = simple_mannaka_birthday(*self._birthdays)
        return date(self._year1, mb.month, mb.day)
