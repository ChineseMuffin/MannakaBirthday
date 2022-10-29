import unittest

from simple_mannaka_birthday import SimpleBirthday, SimpleMannakaBirthday


class Test(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_simple_ignore_leap(self):
        birthday1 = SimpleBirthday(2, 27)
        birthday2 = SimpleBirthday(3, 1)
        expect = SimpleBirthday(2, 28)

        actual = SimpleMannakaBirthday(birthday1, birthday2)

        print(actual)
        self.assertEqual(actual.day, expect.day)
        self.assertEqual(actual.month, expect.month)

    def test_simple_leap_birthday(self):
        birthday1 = SimpleBirthday(2, 29)
        birthday2 = SimpleBirthday(3, 2)
        expect = SimpleBirthday(3, 1)

        actual = SimpleMannakaBirthday(birthday1, birthday2)

        print(actual)
        self.assertEqual(actual.day, expect.day)
        self.assertEqual(actual.month, expect.month)


if __name__ == "__main__":
    unittest.main()
