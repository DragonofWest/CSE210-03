import random
import game.terminal_service

class Jumper:
    """The person falling from the sky 
    
    The responsibility of the jumper is to track the state of the parachute and ?letters guessed so far?
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self, terminal_service):
        """Constructs a new Jumper.

        Args:
            self (Hider): An instance of Hider.
        """
        self.terminal = terminal_service
        self._guess = []
        self.bad_guess_count = 0
        self._parachute = [
            "  _____  ",
            " /_____\ ",
            " \     / ",
            "  \   /  ",
            "    O    ",
            "  / | \  ",
            "   / \   ",
            "         ",
            "^^^^^^^^^"
            ]
    def made_bad_guess(self):
        if self.bad_guess_count >= 5:
            return
        self.bad_guess_count += 1
        self._parachute.pop(0)

    def draw(self):
        if self.bad_guess_count >= 5:
            self.terminal.write_text("    X    ")
        for line in self._parachute:
            self.terminal.write_text(line)


