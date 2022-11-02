from http import client
import os
import discord
from user import Users
from message import Message
from transaction import Transaction
from discord.ext import commands
from dotenv import load_dotenv


intents=discord.Intents.all()
client = commands.Bot(command_prefix='$',intents = intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')

i

if __name__ =='__main__':
    nit_extentions = ['message']

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
    for member in client.get_all_members():
        member_list.append(member)
        
    
    for ext in init_extentions:
        await client.load_extension(ext)

    
       
client.run(TOKEN)