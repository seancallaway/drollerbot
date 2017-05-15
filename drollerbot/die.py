import random

class Die():
    """Defines a Die object for rolling."""

    def __init__(self, sides=20):
        random.seed()
        self.sides=sides

    def roll(self):
        """Rolls the die, returning an integer result."""
        return random.randint(1, self.sides)

