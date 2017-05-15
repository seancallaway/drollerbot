import discord
from discord.ext.commands import Bot
from .die import Die

thebot = Bot(command_prefix=".")

def do_roll(commands):
    result = ""

    try:
        (numdice, remainder) = commands.split('d', 1)
        if '-' in remainder:
            (diesize, modifier) = remainder.split('-', 1)
        elif '+' in remainder:
            (diesize, modifier) = remainder.split('+', 1)
        else:
            diesize = int(remainder)
            modifier = 0
        numdice = int(numdice)
        diesize = int(diesize)
        modifier = int(modifier)

        total = 0

        for i in range(numdice):
            temp = Die(diesize)
            roll = temp.roll()
            total += roll

        result = total + modifier


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
