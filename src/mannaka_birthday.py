from datetime import date, timedelta


"""
誕生日が閏日は未対応
"""


class MannakaBirthday:
    def __init__(self, birthday1, birthday2):

        assert 0 <= (birthday2 - birthday1).days <= 366

        self._birthday1 = birthday1
        self._birthday2 = birthday2

        self._mannaka_date = self.mannaka_date()

    def next(self) -> "MannakaBirthday":
        birthday1_year = self._birthday1.year
        next_birthday1 = self._birthday1.replace(birthday1_year + 1)
        birthday2 = self._birthday2
        return MannakaBirthday(birthday2, next_birthday1)

    def previous(self) -> "MannakaBirthday":
        birthday2_year = self._birthday2.year
        previous_birthday2 = self._birthday2.replace(birthday2_year - 1)
        birthday1 = self._birthday1
        return MannakaBirthday(previous_birthday2, birthday1)

    def mannaka_date(self) -> date:
        date1 = self._birthday1
        date2 = self._birthday2
        delta = date2 - date1
        return date1 + timedelta(delta.days / 2)
