import math
import unittest


def get_ladder_length(*params):
    """
    This function will calculate the ladder length

    Parameters:
    params (list): height(int) and degree(int)

    Returns:
    hypotenuse(int): length of the ladder in inclined position
    """
    height, angle = params
    radian_angle = math.radians(angle)
    hypotenuse = height/math.sin(radian_angle)

    return math.ceil(hypotenuse)


class TestLadderLength(unittest.TestCase):
    def test_get_ladder_length(self):
        """ Test that length of ladder calculated is correct """
        sample = 500
        angle = 70
        expected_result = 533
        test_result = get_ladder_length(sample, angle)
        self.assertEqual(test_result, expected_result)

        sample = 1000
        angle = 10
        expected_result = 5759
        test_result = get_ladder_length(sample, angle)
        self.assertEqual(test_result, expected_result)


if __name__ == '__main__':
    height, angle = map(int, input().split(' '))
    print(get_ladder_length(height, angle))
    unittest.main()
