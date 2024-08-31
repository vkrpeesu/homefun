from game.template import Game, Value


class Solver:

    @staticmethod
    def solve(game: Game) -> dict[int, Value]:
        """
        By exhaustively exploring all positions reachable in the provided game,
        returns a mapping of their encodings to their game-theoretic values in
        a dictionary.
        """
        ...
