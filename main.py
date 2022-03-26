# This code runs a Discord Bot that I made for Science Fair algortihms engineering. The bot is capable of pulling data and educating information using the Wolfram Alpha API and the Wikipedia API that can get data from their sites and bring it to Discord

###########################################################
#  _____                                    _             #
# |  __ \                                  | |            #
# | |__) | __ ___  _ __ ___   ___ _ __ __ _| |_ ___  _ __ #
# |  ___/ '__/ _ \| '_ ` _ \ / _ \ '__/ _` | __/ _ \| '__|#
# | |   | | | (_) | | | | | |  __/ | | (_| | || (_) | |   #
# |_|   |_|  \___/|_| |_| |_|\___|_|  \__,_|\__\___/|_|   #
###########################################################
# Discord bot created by Zaheeb Tariq                     #
# Contact: zaheeb07@gmail.com                             #
###########################################################

import discord # To comunicate with Discord API
import asyncio #To use Async and await functions
import os                           # allows the program to access our desktop, which includes things such as files.
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
import datetime
import psutil
from dotenv import load_dotenv

import random                       # To generate random integers, and choices in an array.
from keep_alive import keepAlive    # To keep the repl from closing automatically.

custom_prefixes = {}
default_prefixes = [';;']

async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes

client = discord.Client()
client = commands.Bot(command_prefix=determine_prefix, help_command=None) 

@client.command()
@commands.guild_only()                                  #Only allow custom prefixs in guild
async def setprefix( ctx, *, prefixes=""):              #Command that allows a server to independently set a prefix, especially useful if bots have conflicting prefixes.
	#if prefixes are not passed then set it to the default
	custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
	embed=discord.Embed(title="Prefix set!",color=green)
	await ctx.send(embed=embed)

green = discord.Color.green()                           # sort of a shortcut for code so instead of having to type out discord.Color.green() just type green. 



@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(';;help'))
  print(f' {client.user} is logged in and ready to RUMBLEEEE!!!!')
          # Message to notify the host that the bot is online.
@client.command()
async def randnum(ctx):#Returns a random number with the user specified limits.
		
    
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel
							 
    embed1=discord.Embed(title="type a number you want to randomize from.", description="Must be the smaller number.", color=green) 
    await ctx.send(embed=embed1)#User sleetcs the first number they want to randomize from. And sets it to the variable x
    msg1 = await client.wait_for("message", check=check)#The bot waits for a user response in chat.
    embed2=discord.Embed(title="Add your second number.", description="Must be greater then the previous number.", color=green) 
    await ctx.send(embed=embed2)#User slects the first number they want to randomize from. Sets to variable y
    msg2 = await client.wait_for("message", check=check)
    x = int(msg1.content) #converts to integer
    y = int(msg2.content)
    if x < y: #A quick check to determine if our fist number x is less then y
        value = random.randint(x,y)
        embed3=discord.Embed(title="Your random number is...", description=f"{value}", color=green)
        await ctx.send(embed=embed3)
    else: embed4=discord.Embed(title="Failed :(", description="Please insure your first number is less then your second number", color=green) # Bring an error if x isnt greater.
    
    await ctx.send(embed=embed4)


load_dotenv()
# Loads cogs intot his main File
# These cogs are in ./commands/ which is where the majority of commands are placed.							
client.load_extension("commands.helpp")

client.load_extension("commands.quote")
client.load_extension("commands.mod")
client.load_extension("commands.wiki")
client.load_extension("commands.fun")
client.load_extension("commands.code")
#keepAlive() #Keeps the repl alive.
TOKEN=os.getenv('DISCORD_TOKEN')
client.run(TOKEN)# Logs in with the providied token from the host's environment.
