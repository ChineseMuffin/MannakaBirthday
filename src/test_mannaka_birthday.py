import unittest
from datetime import date, timedelta

from mannaka_birthday import Birthday, MannakaBirthday


class Test(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_1(self):
        birthday1 = Birthday(3, 1)
        birthday2 = Birthday(2, 28)

        m = MannakaBirthday(birthday1, birthday2, 2000, 2000)

        for i in range(10):
            mannaka = m.mannaka_date()
            m = m.next()
            print(i, mannaka)

        for i in range(5):
            mannaka = m.mannaka_date()
            m = m.previous()
            print(i, mannaka)

    def test_intercalary(self):
        birthday1 = Birthday(2, 29)
        birthday2 = Birthday(2, 29)

        m = MannakaBirthday(birthday1, birthday2, 2000, 2000)

        for i in range(10):
            mannaka = m.mannaka_date()
            m = m.next()
            print(i, mannaka)

        for i in range(5):
            mannaka = m.mannaka_date()
            m = m.previous()
            print(i, mannaka)

    def test_next_previous(self):
        birthday1 = Birthday(3, 1)
        birthday2 = Birthday(2, 28)
        today = date(2022, 10, 29)
        m = MannakaBirthday(birthday1, birthday2, 2000, 2000)

        md = m.mannaka_date()
        print(md)
        md = m.next(today).mannaka_date()
        print(md)
        md = m.previous(today).mannaka_date()
        print(md)


if __name__ == "__main__":
    unittest.main()
