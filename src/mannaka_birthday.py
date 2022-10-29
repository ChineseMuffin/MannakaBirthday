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

        self._year1 = year1
        self._year2 = year2

        self._birthday1 = birthday1
        self._birthday2 = birthday2

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
        has_intercalary = (
            self._birthday1.is_intercalary() or self._birthday2.is_intercalary()
        )

        if has_intercalary:
            if self._birthday1.is_intercalary():
                date1 = date(self._year1, 3, 1)
            else:
                date1 = date(
                    self._year1, self._birthday1.month, self._birthday1.day + 1
                )
            if self._birthday2.is_intercalary():
                date2 = date(self._year2, 3, 1)
            else:
                date2 = date(
                    self._year2, self._birthday2.month, self._birthday2.day + 1
                )
        else:
            date1 = date(self._year1, self._birthday1.month, self._birthday1.day)
            date2 = date(self._year2, self._birthday2.month, self._birthday2.day)

        delta = date2 - date1
        mannaka = date1 + timedelta(delta.days / 2) - timedelta(has_intercalary)

        return mannaka

    def _next_base(self) -> "MannakaBirthday":
        return MannakaBirthday(
            self._birthday2, self._birthday1, self._year2, self._year1 + 1
        )

    def _previous_base(self) -> "MannakaBirthday":
        return MannakaBirthday(
            self._birthday2, self._birthday1, self._year2 - 1, self._year1
        )
