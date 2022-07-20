import unittest


def count_missing_cards(cards):
    """
    This function will count the missing card in the number
    If there is more than two same card in the cards then 
    the counting will be an error

    Parameters:
    cards(string): card labels as a string

    Return:
    (string): GRESKA if there are more than two same cards
    else it will the return the number of missing cards in a suit
    """
    cards_label = [cards[index:index+3] for index in range(0, len(cards), 3)]
    if len(cards_label) != len(set(cards_label)):
        return "GRESKA"
    else:
        labels = "PKHT"
        count_card = [
            13 -
            len([
                card for card in cards_label
                if card[0] == suit
            ])
            for suit in labels

        ]
        return "{} {} {} {}".format(*count_card)


class TestKarte(unittest.TestCase):
    def test_count_missing_cards(self):
        sample = "P01K02H03H04"
        expected_outcome = "12 12 11 13"
        self.assertEqual(count_missing_cards(sample), expected_outcome)

        sample = "H02H10P11H02"
        expected_outcome = "GRESKA"
        self.assertEqual(count_missing_cards(sample), expected_outcome)

        sample = "P01K02H03H04"
        expected_outcome = "12 12 11 13"
        self.assertEqual(count_missing_cards(sample), expected_outcome)


if __name__ == "__main__":
    print(count_missing_cards(input()))
    unittest.main()
