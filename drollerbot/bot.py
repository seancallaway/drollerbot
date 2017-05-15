"""
    bot.py
    ~~~~~~

    Exposes the `thebot` object and does parsing of bot 
    commands.

    :copyright: (c) 2017 by Sean Callaway.
    :license: MIT, see LICENSE for more details.
"""
import discord
from discord.ext.commands import Bot
from .die import Die

thebot = Bot(command_prefix=".")

def do_roll(commands):
    """Perform the roll calculations."""
    
    result = ""
    "".join(commands.split())
    commands = commands.lower()

    try:
        mod = 0
        (numdice, remainder) = commands.split('d', 1)
        if '-' in remainder:
            (diesize, modifier) = remainder.split('-', 1)
            mod = -1
        elif '+' in remainder:
            (diesize, modifier) = remainder.split('+', 1)
            mod = 1
        else:
            diesize = int(remainder)
            modifier = 0

        numdice = int(numdice)
        diesize = int(diesize)
        modifier = int(modifier) * mod

        total = 0

        for i in range(numdice):
            temp = Die(diesize)
            roll = temp.roll()
            result = result + ' (' + str(roll) + ') '
            if i < numdice - 1:
                result = result + "+"
            total += roll

        if modifier < 0:
            result = result + " - " + str(abs(modifier))
        elif modifier > 0:
            result = result + " + " + str(modifier)

        result = result + " = [" + str(total+modifier) + ']'

    except ValueError:
        result = "Usage: .roll #d#(+modifier)"
    except:
        result = "Unexpected error!"
        raise

    return result

@thebot.event
async def on_read():
    print("Client logged in")

@thebot.command()
async def hello(*args):
    return await thebot.say("Hiya, fellas!")

@thebot.command()
async def roll(*, rawdice: str):
    result = do_roll(rawdice)
    return await thebot.say(result)
