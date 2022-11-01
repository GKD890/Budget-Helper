import os
import discord
from typing import Literal, Optional
from discord.ext import commands

intents=discord.Intents.all()

# bot = commands.Bot(command_prefix='$',intents=intents)

intents=discord.Intents.all()
client = commands.Bot(command_prefix='$',intents = intents)

class commandFlag(commands.FlagConverter):
    # memberList:discord.Message.mentions
    member: discord.Member
    amount: float

class viewFlag(commands.FlagConverter):
    # action:Optional[Literal["borrow","lend"]]= None
    # member:Optional[discord.Member] = None
    action:Literal["borrow","lend"] = None
    member:Optional[discord.Member] = None

class Message(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
   
    @client.command()
    async def borrow(self,ctx,*,flags:commandFlag):
        # if other_person.mentioned_in(ctx.message):
            # check if the person is a valid member
        
        mes = f'{ctx.message.author} borrowed {flags.amount} from {flags.member}'
        await ctx.send(mes)

    @client.command()
    async def lend(self,ctx,*,flags:commandFlag):
        # if other_person.mentioned_in(ctx.message):
            # check if the person is a valid member
        
        mes = f'{ctx.message.author} lent {flags.amount} to {flags.member}'
        await ctx.send(mes)
    
    @client.command()
    async def history(self,ctx,*,flags:viewFlag):
        if (flags.action != None):
            if (flags.member != None):
                await ctx.send(f'result of {flags.action} related to {flags.member}: \n')
            else:
                # TODO SELECT from database 
                await ctx.send(f"result related to {flags.action} \n")
        elif (flags.member != None):
            # TODO SELECT from database
            await ctx.send(f'result related to {flags.member}: \n')
        else:
            # TODO SELECT from database
            await ctx.send(f'histroy: \n')





async def setup(bot):
    await bot.add_cog(Message(bot))
    print("message cog added")