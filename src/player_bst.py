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
        if player.name < current_node.player.name:
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
            else:
                return self._insert_recursively(current_node.left, player)
        else:
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
            else:
                return self._insert_recursively(current_node.right, player)

    def search(self, name):
        if self._root is None:
            return self._root
        elif self._root.player.name == name:
            return self._root.player
        else:
            result = self._search_recursively(self._root, name)
            return result

    def _search_recursively(self, current_node, name):
        if name.lower() < current_node.player.name.lower():
            if current_node.left is None:
                return None
            elif current_node.left.player.name.lower() == name.lower():
                return current_node.left.player
            else:
                return self._search_recursively(current_node.left, name)
        else:
            if current_node.right is None:
                return None
            elif current_node.right.player.name.lower() == name.lower():
                return current_node.right.player
            else:
                return self._search_recursively(current_node.right, name)

