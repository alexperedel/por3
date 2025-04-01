import unittest
import random

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

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player('01', "Alice", score=10)
        bob = Player('02', "Bob",  score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(bob < alice)

    def test_successfully_sorting_players(self):
        players = [Player('01', "Alice", score=10), Player('02', "Bob",  score=5),
                   Player('03', "Charlie", score=15), Player('03', "Charlie", score=7),
                   Player('01', "Alice", score=12)]

        manually_sorted_players = [Player('03', "Charlie", score=15), Player('01', "Alice", score=12),
                                   Player('01', "Alice", score=10),  Player('03', "Charlie", score=7),
                                   Player('02', "Bob", score=5)]

        sorted_players = Player.quick_sort(players)

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_successfully_sorting_players_at_scale(self):
        players = [Player(f"Player {i:03}", f"{i}", score=random.randint(0, 1000)) for i in range(1000)]

        correctly_sorted_players = sorted(players, reverse=True)

        custom_algorithm_sorted_players = Player.quick_sort(players)

        self.assertListEqual(custom_algorithm_sorted_players, correctly_sorted_players)
