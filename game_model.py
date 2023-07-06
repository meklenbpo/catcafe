"""
Game Model
"""

from presenter import Presenter


class GameModel:

    def __init__(self, presenter: Presenter) -> None:
        self.presenter = presenter
        self.presenter.game = self
        self.frame = 0
        self.state = 'Terminated'
        return None

    def run_game(self) -> None:
        self.state = 'Running'
        while self.state == 'Running':
            for command in self.presenter.command_queue:
                if command == 'Quit':
                    self.state = 'Terminated'
            self.presenter.command_queue = []
            self.frame += 1
            self.presenter.refresh()
        return None
