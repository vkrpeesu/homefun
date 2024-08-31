from game.template import Game, Value
from typing import Optional


class ZeroBy(Game):

    def __init__(self, args: list[int]):
        self.args = args

    def start() -> int:
        ...

    def get_moves(position: int) -> list[int]:
        ...

    def do_move(position: int, move: int) -> int:
        ...

    def evaluate(position: int) -> Optional[Value]:
        ...
