import unittest


def get_missing_numbers(recited_numbers):
    """
    This function will return the missing numbers

    Parameters:
    recited_numbers(list): list of numbers

    Return:
    missing_numbers(list): missing number in the sequence if any missing number else 'good job'
    """
    max_number = max(recited_numbers)
    sequnce_numbers = set(range(1, max_number+1))
    missing_numbers = sequnce_numbers - set(recited_numbers)
    return ['good job'] if len(missing_numbers) < 1 else sorted(missing_numbers)


class TestMissingNumbers(unittest.TestCase):
    def test_get_missing_number(self):
        """
        This method will test whether missing number function
        """
        sample = [2, 4, 5, 7, 8, 9, 10, 11, 13]
        expected_result = [1, 3, 6, 12]
        test_result = get_missing_numbers(sample)
        self.assertEqual(test_result, expected_result)

        sample = [1, 2, 3, 4, 5]
        expected_result = ['good job']
        test_result = get_missing_numbers(sample)
        self.assertEqual(test_result, expected_result)


if __name__ == '__main__':

    recited_numbers = [int(input()) for _ in range(int(input()))]
    result = get_missing_numbers(recited_numbers)
    print(*result, sep='\n')
    unittest.main()
