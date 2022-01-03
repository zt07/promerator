import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
import random,psutil
from keep_alive import keepAlive
green = discord.Color.green()

def grab_quote(): #defining a fuction here so we can just call or type out "grab_quote()" instead of what is below.
	response = requests.get("https://zenquotes.io/api/random")  #get random quote from zenquotes api
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']  #quote is the data loaded previously
	return (quote)

class quote(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command(aliases=["inspire",'motivate','get_quote'])
	async def quote(self,ctx):
		embed=discord.Embed(title="Here you go!", description=grab_quote(),color=green)
		embed.add_field(name="latency",value=f'{round(self.client.latency * 1000)}ms')
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(quote(client))