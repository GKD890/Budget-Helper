"""
Include all methods of user oeprations
e.g. add or delete users in database, check if users existed once an order created
"""
import discord
import os
import csv
import mariadb


NAMELIST = os.getenv('NAMELIST')
GUILD = os.getenv('DISCORD_GUILD_NAME')
unaddedNamelist = []

class Users():
    def __init__(self) -> None:
        # self.cursor
        self.nameList=set()
        # try:
        conn = mariadb.connect(
                user=os.getenv('DATABASE_USER'),
                password=os.getenv('DATABASE_PASSWORD'),
                host = os.getenv('DATABASE_HOST'),
                port = 3306, # default
                database = os.getenv('DATABASE_NAME'),
                autocommit=True
            )
        self.cursor = conn.cursor()
        # except mariadb.Error as e:
        #     print("Failed to connect with database")
        #     print(f'Database Error: {e}')

    def check_users(self,client:discord.Client,member_list):
    # loop users in namelist file (create one if doesn't exist) and check list
    # if not matched, initialize one
        if (self.cursor != None):
        # Create database and member table for the first time usage
            self.init_database()
            # check if existed member list in current channel
            for member in member_list:
                # if (member.list not in member_list):
                unaddedNamelist.append([member.name,member.id])
                self.nameList.add((member.name,member.id))
            
            print(f"all users checked, {len(unaddedNamelist)} users are not in the database.")

            self.cursor.execute("SELECT name,id FROM {table}".format(table = "member"))
            stored_member_list ={member for member in self.cursor}

            # print(f'stored List: {stored_member_list}')
            # print(f'dynamic List: {self.nameList}')
            print(self.nameList.difference(stored_member_list))
            print(unaddedNamelist)
            print("\n")
            # if unaddedNamelist is not None: #TODO: only add users when confirmed
            #     self.add_users("",self.nameList)
            #     print("finished added")
       
        
    def add_users(self, guild_name,member_list):
        # add a list of users to the table or files
        # create a folder named with guild name
        if (self.cursor != None):
            for member in member_list:
                self.cursor.execute( "INSERT INTO {table} (name,id,borrow,lend) VALUES (?, ?, ?,?) ".format(
                table = "member"), (member[0], member[1],0, 0))

        print("New users have been added")
        
    def init_database(self):
        if (self.cursor != None):
            self.cursor.execute(   "CREATE DATABASE IF NOT EXISTS {database} ; ".format(database = "testDatabase") )

            self.cursor.execute('''CREATE TABLE IF NOT EXISTS {table}(
                name VARCHAR(35),
                id DECIMAL(32) ,
                borrow FLOAT,
                lend FLOAT,
                PRIMARY KEY (id)
            ); '''.format(table = "member") )

            # self.cursor.execute('''CREATE TABLE IF NOT EXISTS {table}(
            #     id INT AUTO_INCREMENT,
            #     person VARCHAR(35),
            #     borrow FLOAT,
            #     lend FLOAT,
            #     trans_date timestamp,
            #     PRIMARY KEY (id),
            #     FOREIGN KEY (person) REFERENCES member(id)
            # );'''.format(table = "record") )
