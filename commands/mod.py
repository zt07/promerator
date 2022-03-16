import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
green = discord.Color.green()

class mod(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def clear(self,ctx, amount=10):
		try:
			if amount > 500:
				await ctx.send("You cant delete that many messages!")  #so it wont lag
			else:
					await ctx.channel.purge(limit=amount)  #clears messages
					embed=discord.Embed(title="Messages cleared!", description=f"{str(amount)} messages deleted!", color=green)
					embed.add_field(name="latency",value=f'{round(self.client.latency * 1000)}ms')
					await ctx.send(embed = embed)
		except:
			embed=discord.Embed(title="failed :(",description="Input a value.",color=green)
			await ctx.send(embed=embed)
				


def setup(client):
	client.add_cog(mod(client))

