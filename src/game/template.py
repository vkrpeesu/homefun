from abc import ABC, abstractmethod
from typing import Optional
from enum import Enum


class Value(Enum):
    """
    Indicates the value of a terminal position in a sequential game.
    """

    WIN = 1
    TIE = 2
    LOSE = 3


class Game(ABC):
    """
    Interface sequential, deterministic, complete-information games.
    """

    @abstractmethod
    def start() -> int:
        """
        Returns an encoding of a game's starting position.
        """
        pass

    @abstractmethod
    def get_moves(position: int) -> list[int]:
        """
        Given a position encoding, returns a list of encodings corresponding
        to moves that can be done from the provided position.
        """
        pass

    @abstractmethod
    def do_move(position: int, move: int) -> int:
        """
        Given a position encoding and a move encoding, returns the encoding of
        the position that would result if the provided move was done from the
        provided position.
        """
        pass

    @abstractmethod
    def evaluate(position: int) -> Optional[Value]:
        """
        Returns the value of the provided position if it is terminal, and None
        in all other cases.
        """
        pass
