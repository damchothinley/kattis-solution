import unittest


def get_number_of_digits(params):
    """
    This function will count and return the number of digits
    in a list

    Parameters:
    params(list): list of estimated cost(int)

    Returns:
    count_digits(list): number of digits for each item in params 
    """
    count_digits = [
        len(cost) for cost in params
    ]
    return count_digits


class TestQuickEstimate(unittest.TestCase):
    def test_get_number_of_digits(self):
        """ Test method to test the number of digits function """
        test_sample = ["314", "1", "5296", "5", "35987"]
        expected_result = [3, 1, 4, 1, 5]
        self.assertEqual(get_number_of_digits(test_sample), expected_result)

        test_sample = ["0", "10", "100"]
        expected_result = [1, 2, 3]
        self.assertEqual(get_number_of_digits(test_sample), expected_result)


if __name__ == '__main__':
    cost = [input() for _ in range(int(input()))]
    print(*get_number_of_digits(cost), sep='\n')
    unittest.main()
