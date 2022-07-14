import unittest


def calculate_ratios(text):
    """
    This function will calcualte ratio of the following
    in a sentence
    1. white space characters represented by _
    2. lowercase letters
    3. uppercase letters
    4. symbols

    Parameters:
    text(string): The sentence to calculate ratios

    Returns:
    ratios(list): the ratios calculated
    """
    total_length = len(text)
    total_white_space = len([char for char in text if char == '_'])
    total_uppercase_letters = len([char for char in text if char.isupper()])
    total_lowercase_letters = len([char for char in text if char.islower()])
    total_symol = len(
        [char for char in text if not char.isalpha() and char != '_']
    )
    formatter = "{:.10f}"
    ratios = [
        formatter.format(total_white_space/total_length),
        formatter.format(total_lowercase_letters/total_length),
        formatter.format(total_uppercase_letters/total_length),
        formatter.format(total_symol/total_length)
    ]
    return ratios


if __name__ == '__main__':
    print(*calculate_ratios(input()), sep='\n')
