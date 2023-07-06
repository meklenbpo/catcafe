"""
Presenter
"""


class Presenter:

    def __init__(self) -> None:
        self.game = None
        self.command_queue = []
        return None

    def refresh(self) -> None:
        raise NotImplementedError
