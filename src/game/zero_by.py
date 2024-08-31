from game.template import Game, Value
from typing import Optional


class ZeroBy(Game):

    def __init__(self, args: list[int]):
        self.args = args

    def start() -> int:

        # TODO: Homefun 1
        ...

    def get_moves(position: int) -> list[int]:

        # TODO: Homefun 1
        ...

    def do_move(position: int, move: int) -> int:

        # TODO: Homefun 1
        ...

    def evaluate(position: int) -> Optional[Value]:

        # TODO: Homefun 1
        ...
