import discord
from discord.ext.commands import Bot

thebot = Bot(command_prefix=".")

@thebot.event
async def on_read():
    print("Client logged in")

@thebot.command()
async def hello(*args):
    return await thebot.say("Hiya, fellas!")

