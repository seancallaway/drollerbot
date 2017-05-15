"""
    die.py
    ~~~~~~

    Implements the Die class for rolling dice.
    This is intended to be extended at some point.

    :copyright: (c) 2017 by Sean Callaway.
    :license: MIT, see LICENSE for more details.
"""
import random

class Die(object):
    """Defines a Die object for rolling."""

    def __init__(self, sides=20):
        random.seed()
        self.sides = sides

    def roll(self):
        """Rolls the die, returning an integer result."""
        return random.randint(1, self.sides)
