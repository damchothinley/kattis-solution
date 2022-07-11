import unittest


def get_fration(dividend, divisor):
    """
    This function will return the mixed fraction after division

    Parameters:
    dividend(int): number to be divided
    divisor(int): number to divide

    Returns
    mixed_fraction (string): r
    returns the mixed fraction after dividing two numbers
    """
    quoient = dividend // divisor
    remainder = dividend % divisor

    return '{} {} / {}'.format(quoient, remainder, divisor)


class TestMixedFraction(unittest.TestCase):
    def test_get_fraction(self):
        """
        This method will test the get mixed fraction function
        """
        sample_divisor = 12
        sample_dividend = 27
        test_result = get_fration(sample_dividend, sample_divisor)
        expected_result = '2 3 / 12'
        self.assertEqual(test_result, expected_result)

        sample_divisor = 98400
        sample_dividend = 2460000
        test_result = get_fration(sample_dividend, sample_divisor)
        expected_result = '25 0 / 98400'
        self.assertEqual(test_result, expected_result)

        sample_divisor = 4000
        sample_dividend = 3
        test_result = get_fration(sample_dividend, sample_divisor)
        expected_result = '0 3 / 4000'
        self.assertEqual(test_result, expected_result)


if __name__ == '__main__':
    while True:
        dividend, divisor = map(int, input().split())
        if not dividend or not divisor:
            break
        print(get_fration(dividend, divisor))
    unittest.main()
