import unittest


def is_valid_cpr_number(ten_digits):
    """
    This function will check whether the given number is valid cpr or not

    Parameters:
    digits(string):10 digit number to check whether cpr_number is valid or not

    Returns
    is_cpr(string): If given digit is cpr_number then it will return 1 else 0
    """
    remove_dash = ''.join(ten_digits.split('-'))
    cpr_number = list(map(int, remove_dash))
    correspond_value = list(map(int, '4327654321'))
    product_and_sum = sum([
        digit * value
        for digit, value in zip(cpr_number, correspond_value)
    ])
    is_valid = (product_and_sum % 11 == 0)
    return '1' if is_valid else '0'


class TestPRNumber(unittest.TestCase):
    def test_is_valid_cpr_number(self):
        """
        This method will test whether a number is valid CPR number or not 
        """
        sample = '070761-4285'
        expected_output = '1'
        test_result = is_valid_cpr_number(sample)
        self.assertEqual(test_result, expected_output)

        sample = '051002-4321'
        expected_output = '0'
        test_result = is_valid_cpr_number(sample)
        self.assertEqual(test_result, expected_output)

        sample = '310111-0469'
        expected_output = '1'
        test_result = is_valid_cpr_number(sample)
        self.assertEqual(test_result, expected_output)


if __name__ == '__main__':
    ten_digits = input()
    print(is_valid_cpr_number(ten_digits))
    unittest.main()
