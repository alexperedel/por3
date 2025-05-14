import unittest

from src.player_bst import PlayerBST
from src.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_bst = PlayerBST()

    def test_insert_players(self):
        players = [Player('01', "Alice", score=10), Player('02', "Bob",  score=7),
                   Player('03', "Charlie", score=15)]

        for player in players:
            self.player_bst.insert(player)

        self.root = self.player_bst.root

        self.assertEqual(self.root.player.uid, '01')
        self.assertEqual(self.root.left.player.uid, '02')
        self.assertEqual(self.root.right.player.uid, '03')

    def test_insert_players_same_scores(self):
        players = [Player('01', "Alice", score=10), Player('02', "Bob",  score=10),
                   Player('03', "Charlie", score=7)]

        for player in players:
            self.player_bst.insert(player)

        self.root = self.player_bst.root

        self.assertEqual(self.root.player.uid, '01')
        self.assertEqual(self.root.right.player.uid, '02')
        self.assertEqual(self.root.left.player.uid, '03')





