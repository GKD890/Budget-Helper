import discord
from discord.ext import commands
import mariadb
import os
import datetime

intents=discord.Intents.all()
client = commands.Bot(command_prefix='$',intents = intents)

class Transaction():
    def __init__(self):
        conn = mariadb.connect(
                user=os.getenv('DATABASE_USER'),
                password=os.getenv('DATABASE_PASSWORD'),
                host = os.getenv('DATABASE_HOST'),
                port = 3306, # default
                database = os.getenv('DATABASE_NAME'),
                autocommit=True
            )
        self.cursor = conn.cursor()

    def record(self,action:str,person_id,other_id,amount:float,description:str):
        if description == None: description = ""
        if self.cursor != None:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO record(person,other_person,{action},trans_date,complete,description) VALUES(?,?,?,?,?,?)".format(
                action = action
            )
            self.cursor.execute(query,(person_id,other_id,amount,time,False,description))
            self.recalculate(person_id)
            self.recalculate(other_id)

    # def lend(self,person_id,other_id,amount,description):
    #     if description == None: description = ""
    #     if self.cursor != None:
    #         time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #         query = "INSERT INTO record(person,other_person,lend,trans_date,complete,description) VALUES(?,?,?,?,?,?)"
    #         self.cursor.execute(query,(person_id,other_id,amount,time,False,description))
    #         self.recalculate(person_id)
    #         self.recalculate(other_id)

    # def repay(self,person_id,other_id,amount):
    #     time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     query = "INSERT INTO record(person,other_person,repay,trans_date,complete) VALUES(?,?,?,?,?)"
    #     self.db.execute(query,(person_id,other_id,amount,time,False))

    def recalculate(self,person_id):
        # callback function everytime 1 record created
        sum_borrow = 0
        sum_lend = 0
        
        self.cursor.execute(" SELECT other_person,lend FROM record WHERE (lend IS NOT NULL AND other_person = {id});".format(
            id= person_id
        ))
        for item in self.cursor.fetchall():
            # print("borrow: ",item)
            sum_borrow += item[1]
        self.cursor.execute(" SELECT other_person,borrow FROM record WHERE (borrow IS NOT NULL AND other_person = {id});".format(
            id= person_id
        ))
        for item in self.cursor.fetchall():
            # print("lend: ",item)
            sum_lend += item[1]
        # update chages of borrow and lend once new record created
        actionList = {("borrow",sum_borrow),("lend",sum_lend)}
        for q in actionList:
            self.cursor.execute(
                "UPDATE member SET {action}={amount} WHERE id = {person_id};".format(
                action = q[0],# action
                amount = q[1],# amount
                person_id = person_id)
            )

   

