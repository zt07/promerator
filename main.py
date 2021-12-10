import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
import DiscordUtils
import random
from keep_alive import keepAlive
'''
This code in documentation enough
'''
#jk

#Written by Zaheeb Tariq courtesy of the above libraries of course zaheeb07@gmail.com though response might take a while

music=DiscordUtils.Music()
client = discord.Client()
client = commands.Bot(command_prefix=';;', help_command=None)  #prefix is ;;, when a user wishes to address the bot, type in ;; then your command EX: ;;play.

green = discord.Color.green()# sort of a shortcut for code so instead of having to type out discord.Color.green() you can just say green. 

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(';;help'))
  print(f' {client.user} is logged in and ready to RUMBLEEEE!!!!')
          #get exited when ready and set status

@client.command()
async def randnum(ctx):

    
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel
							 
    embed1=discord.Embed(title="type a number you want to randomize from.", description="Must be the smaller number.", color=green) 
    await ctx.send(embed=embed1)
    msg1 = await client.wait_for("message", check=check)
    embed2=discord.Embed(title="Add your second number.", description="Must be greater then the previous number.", color=green) 
    await ctx.send(embed=embed2)
    msg2 = await client.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)
    if x < y:
        value = random.randint(x,y)
        embed3=discord.Embed(title="Your random number is...", description=f"{value}", color=green)
        await ctx.send(embed=embed3)
    else: embed4=discord.Embed(title="Failed :(", description="Please insure your first number is less then your second number", color=green) 
    
    await ctx.send(embed=embed4)



'''
pip install py-cord
pip install DiscordUtils[voice]
run = """
pip install py-cord
pip install DiscordUtils[voice]
pip install bython
python main.py
"""
'''															#command list
client.load_extension("commands.helpp")
client.load_extension("commands.music")
client.load_extension("commands.quote")
client.load_extension("commands.mod")
client.load_extension("commands.passcheck")


keepAlive()
my_secret = os.environ['TOKEN']

client.run(os.getenv('TOKEN'))
