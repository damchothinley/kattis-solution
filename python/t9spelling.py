import unittest


def get_key_pressed(user_text):
    """
    This function will return the key presses from

    Paramets:
    user_text(list) : collection of test_cases

    Returns:
    key_pressed(list): the list for the key pressed characters
    """
    keypad = {
        '1': '1',
        'a': '2',
        'd': '3',
        'g': '4',
        'j': '5',
        'm': '6',
        'p': '7',
        't': '8',
        'w': '9',
        '*': '*',
        '0': '0',
        '+': '00',
        '#': '#',
        ' ': '0'
    }
    key_pressed = [
        [
            keypad[letter] if letter in keypad.keys()
            else keypad[chr(ord(letter) - 1)] * 2 if chr(ord(letter) - 1) in keypad.keys()
            else keypad[chr(ord(letter) - 2)] * 3 if chr(ord(letter) - 2) in keypad.keys()
            else keypad[chr(ord(letter) - 3)] * 4
            for letter in word
        ] for word in user_text
    ]
    insert_pause = [
        ''.join([
            '{} '.format(item)
            if index != len(row) and item[0] == row[index][0]
            else item
            for index, item in enumerate(row, start=1)
        ])for row in key_pressed
    ]
    result = [
        'Case #{}: {}'.format(index, row) for index, row in enumerate(insert_pause, start=1)]
    return result


class TestT9Spelling(unittest.TestCase):
    def test_get_key_pressed(self):

        sample = ['hi', 'yes', 'foo  bar', 'hello world']
        expected_output = [
            "Case #1: 44 444",
            "Case #2: 999337777",
            "Case #3: 333666 6660 022 2777",
            "Case #4: 4433555 555666096667775553",
        ]
        test_result = get_key_pressed(sample)
        self.assertEqual(expected_output, test_result)


if __name__ == '__main__':
    # messages = [
    #     input() for _ in range(int(input()))
    # ]
    # print(*get_key_pressed(messages), sep='\n')
    unittest.main()
