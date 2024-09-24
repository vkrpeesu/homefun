from game.template import Game, Value
from dataclasses import dataclass


@dataclass
class SolutionRecord:
    """
    Data regarding a specific position in a sequential game.
    """

    value: Value

class Value(

class TicTacToe(Game):
    def __init__(self):
        self.board_size = 3
        self.memory = [0] * 9

    def start(self):
        return 0

    def get_moves(self, position: int):
        return [i for i in range(9) if self.board[i] == 0]


    def move(self, move: int, player: int):
        if self.board[move] == 0:
            self.board[move] = player

    def value(self):
        winner = self.check_winner()
        if winner == 1:
            return Value.WIN
        elif winner == 2:
            return Value.LOSE
        elif self.is_full():
            return Value.TIE
        return None

    def check_winner(self):
        winning_board = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 1, 2], [3, 4, 5], [6, 7, 8]
        ]
        for item in winning_board:
            if self.board(combo[0] == self.board[combo[1]] == self.board[combo[2]] != 0:
                return self.board[combo[0]]
            return 0

    def is_full(self):
        return all(cell != 0 for cell in self.baord)

    def get_cell(self, index: int):
        return self.board[index]
             
class Solver:

    @staticmethod
    def solve(game: TicTacToe, position: int = None, player: int = 1):
        solution = {}
        Solver.__explore(game, game.start(), solution)
        return solution

    def __explore(game: Game, position: int, solution: dict[int, SolutionRecord]):
        if position in solutions:
            return

        value = game.value(position)
        if value is not Value.MEDIAL:
            solution[position] = SolutionRecord(value=terminal_value)
            return

        for move in game.get_moves(position):
            new_position = game.move(position, move)
            Solver.__explore(game, new_position, solution)

        solution[position] = SolutionRecord(value=Value.MEDIAL)
        
        
        """
        By exhaustively exploring all positions reachable in the provided game,
        returns a mapping of their encodings to their game-theoretic values in
        a dictionary (and other information we may care about).
        """
