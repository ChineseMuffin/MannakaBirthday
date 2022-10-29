from datetime import date, timedelta
from dataclasses import dataclass


@dataclass
class Birthday:
    month: int
    day: int

    def is_intercalary(self):
        return self.day == 29 and self.month == 2


class MannakaBirthday:
    MAX_ITERATION = 4000

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
            for _ in range(MannakaBirthday.MAX_ITERATION):
                is_past = m.mannaka_date() < target
                if is_past:
                    return m._next_base()
                m = m.previous()

        if delta_days < 0:
            for _ in range(MannakaBirthday.MAX_ITERATION):
                is_future = m.mannaka_date() > target
                if is_future:
                    return m
                m = m._next_base()

        raise Exception()

    def previous(self, target: date | None = None) -> "MannakaBirthday":
        if target is None:
            return self._previous_base()

        return self.next(target)._previous_base()

    def mannaka_date(self) -> date:
        has_intercalary = any(b.is_intercalary() for b in self._birthdays)

        if has_intercalary:

            def calibed_next_date(year: int, birthday: Birthday) -> date:
                if birthday.is_intercalary():
                    return date(year, 3, 1)
                return date(year, birthday.month, birthday.day + 1)

            date1, date2 = (
                calibed_next_date(y, b) for y, b in zip(self._years, self._birthdays)
            )

        else:
            date1, date2 = (
                date(y, b.month, b.day) for y, b in zip(self._years, self._birthdays)
            )

        delta = date2 - date1
        mannaka = date1 + timedelta(delta.days / 2) - timedelta(has_intercalary)

        return mannaka

    def _next_base(self) -> "MannakaBirthday":
        return MannakaBirthday(
            self._birthdays[1], self._birthdays[0], self._years[1], self._years[0] + 1
        )

    def _previous_base(self) -> "MannakaBirthday":
        return MannakaBirthday(
            self._birthdays[1], self._birthdays[0], self._years[1] - 1, self._years[0]
        )
