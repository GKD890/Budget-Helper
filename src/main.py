from http import client
import os
import discord
from user import Users
from debug import Deb
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands

intents=discord.Intents.all()
client = commands.Bot(command_prefix='!',intents = intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')

init_extentions = []


if __name__ =='__main__':
    for ext in init_extentions:
        client.load_extension(ext)

        
client.run(TOKEN)