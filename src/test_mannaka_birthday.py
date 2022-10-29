import unittest
from datetime import date, timedelta

from mannaka_birthday import MannakaBirthday


class Test(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_1(self):
        birthday1 = date(2000, 2, 28)
        birthday2 = date(2000, 3, 1)

        m = MannakaBirthday(birthday1, birthday2)

        for i in range(10):
            mannaka = m.mannaka_date()
            m = m.next()
            print(mannaka)

        for i in range(5):
            mannaka = m.mannaka_date()
            m = m.previous()
            print(mannaka)

    def test_intercalary(self):
        birthday1 = date(2000, 2, 29)
        birthday2 = date(2000, 2, 29)

        m = MannakaBirthday(birthday1, birthday2)

        for i in range(10):
            mannaka = m.mannaka_date()
            m = m.next()
            print(mannaka)

        for i in range(5):
            mannaka = m.mannaka_date()
            m = m.previous()
            print(mannaka)


if __name__ == "__main__":
    unittest.main()
