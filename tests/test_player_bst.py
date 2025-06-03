import unittest

from src.player_bst import PlayerBST
from src.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_bst = PlayerBST()

    def test_insert_players(self):
        players = [Player('01', "Bob", score=10), Player('02', "Alice",  score=7),
                   Player('03', "Charlie", score=15)]

        for player in players:
            self.player_bst.insert(player)

        self.root = self.player_bst.root

        self.assertEqual(self.root.player.uid, '01')
        self.assertEqual(self.root.left.player.uid, '02')
        self.assertEqual(self.root.right.player.uid, '03')

    def test_insert_players_same_names(self):
        players = [Player('01', "Alice", score=10), Player('02', "Alice",  score=10),
                   Player('03', "Charlie", score=7)]

        for player in players:
            self.player_bst.insert(player)

        self.root = self.player_bst.root

        self.assertEqual(self.root.player.uid, '01')
        self.assertEqual(self.root.right.player.uid, '02')
        self.assertEqual(self.root.right.right.player.uid, '03')


    def test_search_players(self):
        players = [Player('01', "Bob", score=10), Player('02', "Alice",  score=7),
                   Player('03', "Charlie", score=15)]

        for player in players:
            self.player_bst.insert(player)

        self.player_object = self.player_bst.search("Alice")

        self.assertEqual(self.player_object.name, 'Alice')

    def test_search_players_non_existing_name(self):
        players = [Player('01', "Alice", score=10), Player('02', "Bob",  score=10),
                   Player('03', "Charlie", score=7)]

        for player in players:
            self.player_bst.insert(player)

        self.root = self.player_bst.root

        self.player_object = self.player_bst.search("Alex")

        self.assertIsNone(self.player_object)

    def test_balance_bst_collects_players(self):
        players = [
            Player('01', "Liam", score=50),
            Player('02', "Emma", score=30),
            Player('03', "Noah", score=70),
            Player('04', "Olivia", score=20),
            Player('05', "William", score=40),
            Player('06', "Ava", score=60),
            Player('07', "James", score=80),
            Player('08', "Sophia", score=10),
            Player('09', "Benjamin", score=25),
            Player('10', "Isabella", score=35),
            Player('11', "Lucas", score=45),
            Player('12', "Mia", score=55),
            Player('13', "Henry", score=65),
            Player('14', "Charlotte", score=75),
            Player('15', "Alexander", score=85),
        ]

        for player in players:
            self.player_bst.insert(player)

        self.root = self.player_bst.root

        self.player_bst.balance_bst()

        result_list = []
        self.player_bst._bst_convertor_to_list(result_list, self.root)

        self.assertEqual(len(result_list), len(players))

