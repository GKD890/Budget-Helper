import os
import discord
from user import Users
from debug import Deb
from transaction import Transaction

from dotenv import load_dotenv
from discord.ext import commands

intents=discord.Intents.all()

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')

client = discord.Client(intents = intents)
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
    for member in client.get_all_members():
        member_list.append(member)
        print("member: ", member)
    userIns = Users()
    userIns.check_users(client,member_list)
    trans = Transaction(client)
    trans.borrow("982154651673722911","518213197602357281",203.3,"test debt")
    trans.lend("982154651673722911","518213197602357281",1,"test debt23")


# bot = commands.Bot(command_prefix='!',intents = intents)

@client.event
async def on_message(message):
    # allocate message based on different command 
    if message.author == client.user:
        return
    welcome_phrase = [
        "hi",
        "hi!",
        "hello",
        "hello!",
        "test:message"
    ]
    if (message.content in welcome_phrase):
    # if (message.content == 'hi'):
        print("matched message")
        # response = Deb.message_info.format(message.created_at,message.author,message.id)
        response = "date: {date} \n author: {author} \n ID: {ID}".format(date = message.created_at,author = message.author,ID = message.id)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)
