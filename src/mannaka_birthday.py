from datetime import date, timedelta

from simple_mannaka_birthday import (
    Birthday,
    mannaka_birthday as simple_mannaka_birthday,
)


class MannakaBirthday:
    CALIB = timedelta(1)

    def __init__(
        self, birthday1: Birthday, birthday2: Birthday, year1: int, year2: int
    ):
        assert year1 <= year2

        self._years = (year1, year2)

        self._birthdays = (birthday1, birthday2)

    def next(self, target: date | None = None) -> "MannakaBirthday":
        if target is None:
            return self._next_base()

        m = self

        delta_days = (m.mannaka_date() - target).days

        if delta_days == 0:
            return m

        if delta_days > 0:
            m_next = m
            for _ in range(abs(delta_days)):
                if m.mannaka_date() < target:
                    return m_next
                m_next = m
                m = m._previous_base()

        if delta_days < 0:
            for _ in range(abs(delta_days)):
                if m.mannaka_date() > target:
                    return m
                m = m._next_base()

        raise Exception()

    def previous(self, target: date | None = None) -> "MannakaBirthday":
        if target is None:
            return self._previous_base()

        return self.next(target)._previous_base()

    def mannaka_date(self) -> date:
        date1, date2 = (
            self.calibed_next_date(y, b) for y, b in zip(self._years, self._birthdays)
        )

        delta = date2 - date1
        mannaka = date1 + timedelta(delta.days / 2) - self.CALIB

        return mannaka

    @classmethod
    def calibed_next_date(cls, year: int, birthday: Birthday) -> date:
        if is_intercalary(birthday):
            return date(year, 3, 1)
        return date(year, birthday.month, birthday.day) + cls.CALIB

    def _next_base(self) -> "MannakaBirthday":
        return MannakaBirthday(*self._birthdays, self._years[1], self._years[0] + 1)

    def _previous_base(self) -> "MannakaBirthday":
        return MannakaBirthday(*self._birthdays, self._years[1] - 1, self._years[0])


class SimpleMannakaBirthday:
    def __init__(
        self, birthday1: Birthday, birthday2: Birthday, year1: int, year2: int
    ):
        self._year1 = year1
        self._birthdays = birthday1, birthday2

    def mannaka_date(self) -> date:
        mb = simple_mannaka_birthday(*self._birthdays)
        return date(self._year1, mb.month, mb.day)


def is_intercalary(birthday: Birthday) -> bool:
    return birthday.day == 29 and birthday.month == 2
