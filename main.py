"""
Game
"""

import sys

from game_model import GameModel
from terminal_presenter import TerminalPresenter


def main() -> int:
    ascii_presenter = TerminalPresenter()
    game = GameModel(ascii_presenter)
    game.run_game()
    return 0


if __name__ == '__main__':
    sys.exit(main())
