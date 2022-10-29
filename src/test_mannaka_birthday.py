import unittest
from datetime import date

from mannaka_birthday import Birthday, MannakaBirthday, SimpleMannakaBirthday


class Test(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_1(self):
        birthday1 = Birthday(2, 28, 2000)
        birthday2 = Birthday(3, 1, 2000)

        m = MannakaBirthday(birthday1, birthday2)

        for i in range(10):
            mannaka = m.to_date()
            print(i, mannaka)
            m = m.next()

        for i in range(5):
            mannaka = m.to_date()
            print(i, mannaka)
            m = m.previous()

    def test_intercalary(self):
        birthday1 = Birthday(2, 28, 2000)
        birthday2 = Birthday(2, 29, 2000)

        m = MannakaBirthday(birthday1, birthday2)

        for i in range(10):
            mannaka = m.to_date()
            print(i, mannaka)
            m = m.next()

        for i in range(5):
            mannaka = m.to_date()
            print(i, mannaka)
            m = m.previous()

    def test_next_previous_past(self):
        birthday1 = Birthday(2, 28, 2000)
        birthday2 = Birthday(3, 1, 2000)
        today = date(2022, 10, 29)
        m = MannakaBirthday(birthday1, birthday2)

        expect = iter((date(2023, 2, 28), date(2022, 8, 30)))

        md = m.next(today).to_date()
        print(md)
        self.assertEqual(md, next(expect))

        md = m.previous(today).to_date()
        print(md)
        self.assertEqual(md, next(expect))

    def test_next_previous_future(self):
        birthday1 = Birthday(2, 28, 2100)
        birthday2 = Birthday(3, 1, 2100)
        today = date(2022, 10, 29)
        m = MannakaBirthday(birthday1, birthday2)

        expect = iter((date(2023, 2, 28), date(2022, 8, 30)))

        md = m.next(today).to_date()
        print(md)
        self.assertEqual(md, next(expect))

        md = m.previous(today).to_date()
        print(md)
        self.assertEqual(md, next(expect))

    def test_simple(self):
        year = 2000
        hanamaru = Birthday(3, 4, year)
        mari = Birthday(6, 13, year)

        expect = date(year, 10, 23)

        m = SimpleMannakaBirthday(hanamaru, mari)
        md = m.to_date()

        print(md)
        self.assertEqual(md, expect)


if __name__ == "__main__":
    unittest.main()
