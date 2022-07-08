import unittest


def get_decode_sentence(encoded_sentence):
    """
    This function will return the sentence decode

    Parameters:
    encoded_sentence(str):  Luka's encoded string

    Return
    message(str): decoded string
    """
    encoded_technique = ["apa", "epe", "ipi", "opo", "upu"]

    for item in encoded_technique:
        encoded_sentence = encoded_sentence.replace(item, item[0])
    return encoded_sentence


class TestKemija(unittest.TestCase):
    def test_get_decoded_string(self):
        """
        Test function to that will check the decoded sentence 
        """
        sample = 'zepelepenapa papapripikapa'
        result = 'zelena paprika'
        self.assertEqual(get_decode_sentence(sample), result)


if __name__ == '__main__':
    print(get_decode_sentence(input()))
    unittest.main()
