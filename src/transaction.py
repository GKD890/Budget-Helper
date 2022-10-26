import discord
from discord.ext import commands
import mariadb
import os

intents=discord.Intents.all()
client = commands.Bot(command_prefix='!',intents = intents)

class Transaction(commands.Cog):
    def __init__(self,client:discord.Client):
        self.client = client
        self.db
        try:
            self.db = mariadb.connect(
                user=os.getenv('DATABASE_USER'),
                password=os.getenv('DATABASE_PASSWORD'),
                host = os.getenv('DATABASE_HOST'),
                port = 3306, # default
                database = os.getenv('DATABASE_NAME'),
                autocommit=True
            ).cursor()
        except mariadb.Error as e:
            print("Failed to connect with database")
            print(f'Database Error: {e}')
    ###
    
    # @commands.Cog.listener()
    # async def borrow(self,client):
        
    # @commands.command()
    # async def borrow(self,ctx):
    #     obj = ctx.mentions()
    #     for person in obj:
    #         # call the database function to add transactions

    #         #TODO
    #         ctx.send("")

    def borrow(self,person_id,amount):
        query = "INSERT INTO {table} (id,borrow,lend) VALUES (?, ?, ?);"
        self.db.excute(query,(person_id,amount,0))
    
def setup(client):
    client.add_cot(Transaction(client))
   

