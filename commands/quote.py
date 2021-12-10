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
green = discord.Color.green()

def grab_quote(): #defining a fuction here so we can just call or type out "grab_quote()" instead of what is below.
    response = requests.get(
        "https://zenquotes.io/api/random")  #get stuff from zenquotes api
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0][
        'a']  #quote is the data loaded previously
    return (quote)

class quote(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command()
	async def quote(self,ctx):
		embed=discord.Embed(title="Here you go!", description=grab_quote(),color=green)
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(quote(client))