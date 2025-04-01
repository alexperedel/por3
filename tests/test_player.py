import unittest

from src.player import Player

class TestPlayer(unittest.TestCase):
    def test_sort_players(self):
        players = [Player('01', "Alice", score=10), Player('02', "Bob",  score=5),
                   Player('03', "Charlie", score=15)]
        # note: ensure initialization code is valid for **your** implementation

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player('02', "Bob",  score=5), Player('01', "Alice", score=10),
                                    Player('03', "Charlie", score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)