import asyncio
import os
import discord
from user import Users
from debug import Deb
from transaction import Transaction
from message import Message

from dotenv import load_dotenv
from discord.ext import commands

intents=discord.Intents.all()

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')

# client = discord.Client(intents = intents)
client = commands.Bot(command_prefix='$',intents = intents)
# client = commands.bot(command_prefix='!',intents = intents)
                               
member_list = []
global GUILD_ID 
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} has connected to guild: \n'
        f'{guild.name}(id: {guild.id})\n'
    )
    # get member list
    
        
    await client.load_extension('message')

  

client.run(TOKEN)
