import os
import discord
from discord.ext import commands

intents=discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents = intents)

intents=discord.Intents.all()
client = commands.Bot(command_prefix='!',intents = intents)

class Message(commands.Cog):
    def __init__(self) -> None:
        super().__init__()

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
        
        ### PASTE from transaction
            
        # @commands.Cog.listener()
        # async def borrow(self,client):
            
        # @commands.command()
        # async def borrow(self,ctx):
        #     obj = ctx.mentions()
        #     for person in obj:
        #         # call the database function to add transactions

        #         #TODO
        #         ctx.send("")
def setup(client):
    client.add_cot(Message(client))