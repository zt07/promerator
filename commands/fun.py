import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
green = discord.Color.green()

responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]

class fun(commands.Cog):
	def __init__(self,client):
		self.client=client
	
	@commands.command()
	async def eight_ball(self, ctx,query):
		embed=discord.Embed(title=random.choice(responses),color=green)
		embed.add_field(name="latency",value=f'{round(self.client.latency * 1000)}ms')
		await ctx.send(embed=embed)

	@commands.command()
	async def coinflip(self, ctx):
			sides=["heads","tails"]
			embed=discord.Embed(title="Flipping",description=random.choice(sides),color=green)
			embed.add_field(name="latency",value=f'{round(self.client.latency * 1000)}ms')
			await ctx.send(embed=embed)


def setup(client):
	client.add_cog(fun(client))
