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

class mod(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def clear(self,ctx, amount=10):
		if amount > 500:
			await ctx.send("You cant delete that many messages!")  #so it wont lag
		else:
				await ctx.channel.purge(limit=amount)  #clears messages
				embed=discord.Embed(title="Messages cleared!", description=f"{str(amount)} messages deleted!", color=green)
				await ctx.send(embed = embed)	

def setup(client):
	client.add_cog(mod(client))

