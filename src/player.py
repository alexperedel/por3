class Player:
    """Represents a player with a unique ID, name and score."""

    def __init__(self, unique_id: str, player_name: str, score: int):
        self._unique_id = unique_id
        self._player_name = player_name
        self._score = score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    @property
    def uid(self):
        return self._unique_id

    @property
    def name(self):
        return self._player_name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score: int):
        if new_score < 0:
            raise ValueError("Score must be a positive number!")
        self._score = new_score

    def __str__(self):
        return f"Player {self._player_name} (ID: {self._unique_id})"
