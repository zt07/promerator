import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
import wikipedia
import wolframalpha
green = discord.Color.green()
#Searches wikipedia page and returns it in Discord.
app_id=os.environ['Wolframaplha_appid']

client=wolframalpha.Client(app_id)
class wiki(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command()
	async def wiki_summary(self,ctx,search):
		try:
			result=wikipedia.summary(search,sentences=3,chars=300,auto_suggest=True,redirect=True)
			embed=discord.Embed(title="Fetching results...",description=result,color=green)
			embed.add_field(name="latency",value=f'{round(self.client.latency * 1000)}ms')#returns latency
			await ctx.send(embed=embed)
		except:
			embed=discord.Embed(title="No results:(",description="Try a valid search",color=green)
			await ctx.send(embed=embed)
			
	@commands.command()
	async def search(self,ctx,*,ques):
		embed=discord.Embed(title="Searching...",color=green)
		await ctx.send(embed=embed)
		res=client.query(ques)
		try:
			answer = next(res.results).text
			await ctx.channel.purge(limit=1)
			embed=discord.Embed(title="Answer:",description=answer,color=green)
			await ctx.send(embed=embed)
		except StopIteration:
			await ctx.channel.purge(limit=1)
			embed=discord.Embed(title="No results:(",color=green)
			await ctx.send(embed=embed)
	



def setup(client):
	client.add_cog(wiki(client))