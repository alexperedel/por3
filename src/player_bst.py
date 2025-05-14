from .player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player):
        if self._root is None:
            self._root = PlayerBNode(player)
        else:
            self._insert_recursively(self._root, player)

    def _insert_recursively(self, current_node, player):
        if player.score < current_node.player.score:
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
            else:
                return self._insert_recursively(current_node.left, player)
        else:
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
            else:
                return self._insert_recursively(current_node.right, player)