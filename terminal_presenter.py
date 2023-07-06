"""
Terminal Presenter
"""

import time

import keyboard

from presenter import Presenter


class TerminalPresenter(Presenter):

    def refresh(self) -> None:
        print(self.game.frame)
        if keyboard.is_pressed('q'):
            self.command_queue.append('Quit')
        time.sleep(0.1)
        return None
