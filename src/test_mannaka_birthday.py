import unittest
from datetime import date, timedelta

from mannaka_birthday import Birthday, MannakaBirthday, SimpleMannakaBirthday


class Test(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_1(self):
        birthday1 = Birthday(3, 1)
        birthday2 = Birthday(2, 28)

        m = MannakaBirthday(birthday1, birthday2, 2000, 2000)

        for i in range(10):
            mannaka = m.mannaka_date()
            print(i, mannaka)
            m = m.next()

        for i in range(5):
            mannaka = m.mannaka_date()
            print(i, mannaka)
            m = m.previous()

    def test_intercalary(self):
        birthday1 = Birthday(2, 28)
        birthday2 = Birthday(2, 29)

        m = MannakaBirthday(birthday1, birthday2, 2000, 2000)

        for i in range(10):
            mannaka = m.mannaka_date()
            print(i, mannaka)
            m = m.next()

        for i in range(5):
            mannaka = m.mannaka_date()
            print(i, mannaka)
            m = m.previous()

    def test_next_previous(self):
        birthday1 = Birthday(3, 1)
        birthday2 = Birthday(2, 28)
        today = date(2022, 10, 29)
        m = MannakaBirthday(birthday1, birthday2, 2000, 2000)

        expect = iter((date(2000, 2, 29), date(2023, 2, 28), date(2022, 8, 30)))

        md = m.mannaka_date()
        print(md)
        self.assertEqual(md, next(expect))

        md = m.next(today).mannaka_date()
        print(md)
        self.assertEqual(md, next(expect))

        md = m.previous(today).mannaka_date()
        print(md)
        self.assertEqual(md, next(expect))

    def test_simple(self):
        hanamaru = Birthday(3, 4)
        mari = Birthday(6, 13)
        year = 2000

        expect = date(year, 10, 23)

        m = SimpleMannakaBirthday(hanamaru, mari, year, year)
        md = m.mannaka_date()

        print(md)
        self.assertEqual(md, expect)


if __name__ == "__main__":
    unittest.main()
