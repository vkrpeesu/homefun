from cli import Cli, Args, GameImplementation
from game.template import Value
from game.zero_by import ZeroBy
from typing import Optional
from solver import Solver


if __name__ == "__main__":

    arguments: Args = Cli.parse()
    value: Optional[Value] = None

    match arguments.game:
        case GameImplementation.zero_by:
            game = ZeroBy(arguments.input)
            solution = Solver.solve(game)
