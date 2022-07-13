import unittest


def get_types_of_sum(params):
    """
    This function will calculate and return the following types of sum
    1. sum of the range for the given number
    2. all the even numbers sum within that range
    3. all the odd numbers sum within that range

    Parameters:
    params(List):
    each row contain sequence numbers and number to find the sum

    Returns:
    all_sums(list): stores the calculated sum and return at once
    """
    all_sums = []
    for row in params:
        set_number, find_sum_number = map(int, row.split(' '))
        range_sum = sum(range(1, find_sum_number+1))
        even_sum = range_sum * 2
        odd_sum = even_sum - find_sum_number
        all_sums.append(
            "{} {} {} {}".format(
                set_number, range_sum, odd_sum, even_sum
            )
        )
    return all_sums


class TestSumKindOfProblem(unittest.TestCase):
    def test_get_types_of_sum(self):
        """
        Test the function get_type_of_sum here
        """
        sample_data = [
            "1 1",
            "2 10",
            "3 1001",
        ]
        expected_result = [
            "1 1 1 2",
            "2 55 100 110",
            "3 501501 1002001 1003002",
        ]
        test_result = get_types_of_sum(sample_data)
        self.assertEqual(expected_result, test_result)


if __name__ == "__main__":
    dataset_count = int(input())
    user_input = [
        input() for _ in range(dataset_count)
    ]
    print(*get_types_of_sum(user_input), sep='\n')
    unittest.main()
