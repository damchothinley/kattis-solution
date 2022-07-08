import unittest
from datetime import datetime


def get_day_of_week(day, month):
    """
    This function will return the day of the date
    in the year 2009
    """
    day_of_week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday',
    }
    day_in_number = datetime(2009, month, day).isoweekday()

    return day_of_week.get(day_in_number)


class TestDatum(unittest.TestCase):
    def test_get_day_of_week(self):
        sample_test = get_day_of_week(1, 1)
        self.assertEqual(sample_test, 'Thursday')

        sample_test = get_day_of_week(17, 1)
        self.assertEqual(sample_test, 'Saturday')

        sample_test = get_day_of_week(25, 9)
        self.assertEqual(sample_test, 'Friday')


if __name__ == '__main__':
    date, month = map(int, input().split(' '))
    print(get_day_of_week(date, month))
    unittest.main()
