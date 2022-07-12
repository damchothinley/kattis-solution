import unittest


def get_binary_watch(given_time):
    """
    This function will return a time in binary format
    and binary 1's is represented by astreik(*) and 0's by dots(.)

    Parmeters:
    given_time(string): 24hour format time to be converted to binary

    Returns:
    binary_time(str): time converted to binary string using * and .
    """
    hours_and_minutes = [
        bin(int(num))[2:].zfill(4) for num in given_time
    ]
    fill_with_shape = [
        ''.join(['.' if num == '0' else '*' for num in item])
        for item in hours_and_minutes

    ]
    hours, minutes = [
        fill_with_shape[i:i+2]
        for i in range(0, len(fill_with_shape), 2)
    ]
    hours = [' '.join(item) for item in zip(*hours)]
    minutes = [' '.join(item) for item in zip(*minutes)]
    result = [
        "   ".join([item_hours, item_minutes])
        for item_hours, item_minutes in zip(hours, minutes)
    ]
    return '\n'.join(result)


class TestBinaryWatch(unittest.TestCase):
    def test_get_binary_watch(self):
        """
        This function will test the get binary watch function
        """
        sample_data = '1615'
        expected_result = ". .   . .\n. *   . *\n. *   . .\n* .   * *"
        test_result = get_binary_watch(sample_data)
        self.assertEqual(test_result, expected_result)

        sample_data = '1900'
        expected_result = ". *   . .\n. .   . .\n. .   . .\n* *   . ."
        test_result = get_binary_watch(sample_data)
        self.assertEqual(test_result, expected_result)

        sample_data = '0830'
        expected_result = ". *   . .\n. .   . .\n. .   * .\n. .   * ."
        test_result = get_binary_watch(sample_data)
        self.assertEqual(test_result, expected_result)


if __name__ == '__main__':
    print(get_binary_watch(input()))
    unittest.main()
