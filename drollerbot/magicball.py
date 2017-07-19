"""
    magicball.py
    ~~~~~~~~

    Exposes the `MagicBall` object.

    :copyright: (c) 2017 by Sean Callaway.
    :license: MIT, see LICENSE for more details.
"""
import random

class MagicBall(object):
    """Defines a magic 8 ball."""

    def __init__(self):
        """Setup the 8ball with responses."""
        random.seed()
        self.responses = [
                           'It is certain.', 
                           'It is decidedly so.',
                           'Without a doubt.',
                           'Yes, definitely.',
                           'You may rely on it.',
                           'As I see it, yes.',
                           'Most likely.',
                           'Outlook good.',
                           'Yes.',
                           'Signs point to yes.',

                           'Reply hazy. Try again.',
                           'Ask again later',
                           'Better not tell you now.',
                           'Cannot predict now.',
                           'Concentrate and ask again.',

                           'Don\'t count on  it.',
                           'My reply is no.',
                           'My sources say no.',
                           'Outlook not so good.',
                           'Very doubtful.',
                         ]

    def shake(self):
        """Shake the 8ball and get a response."""
        return self.responses[random.randint(1, len(self.responses))]
