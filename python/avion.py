import unittest


def get_cia_blimps(registration_codes):
    """
    This function will look for the word "FBI" in each row

    Parameters:
    registration_codes(list): list of 5 rows of codes(string)

    Return:
    rows_with_blimps(list): row number with the registation CIA blimps 
    else "HE GOT AWAY"
    """
    rows_with_blimps = [
        index for index, row in enumerate(registration_codes, start=1)
        if "FBI" in row
    ]
    return rows_with_blimps if len(rows_with_blimps) else ["HE GOT AWAY!"]


class TestAvion(unittest.TestCase):
    def test_get_cia_blimps(self):
        """
        Test method to check get_cia_blimps function
        """
        sample = [
            "N-FBI1",
            "9A-USKO",
            "I-NTERPOL",
            "G-MI6",
            "RF-KGB1"
        ]
        expected_result = [1]
        test_result = get_cia_blimps(sample)
        self.assertEqual(test_result, expected_result)

        sample = [
            "N321-CIA",
            "F3-B12I",
            "F-BI-12",
            "OVO-JE-CIA",
            "KRIJUMCAR1"
        ]
        expected_result = ["HE GOT AWAY!"]
        test_result = get_cia_blimps(sample)
        self.assertEqual(test_result, expected_result)

        sample = [
            "47-FBI",
            "BOND-007",
            "RF-FBI18",
            "MARICA-13",
            "13A-FBILL"
        ]
        expected_result = [1, 3, 5]
        test_result = get_cia_blimps(sample)
        self.assertEqual(test_result, expected_result)


if __name__ == '__main__':
    codes = [input() for _ in range(5)]
    result = get_cia_blimps(codes)
    print(*result, sep=' ')
    unittest.main()
