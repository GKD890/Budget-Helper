import os
import discord
from discord.ext import commands

intents=discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents = intents)

@bot.event
async def on_message(message,client:discord.Client):
    # allocate message based on different command 
    author = message.author
    if author == client.user:
        return
    who_to_send = mess

    if (message.content in welcome_phrase): #TODO: set functions and prefix
    # if (message.content == 'hi'):
        print("matched message")
        response = 'nmsl'
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException