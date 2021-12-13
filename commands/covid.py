import discord # To comunicate with Discord API
import asyncio #To use Async and await functions
import os # allows the program to access our desktop, which includes things such as files.
import json # JavaScript Object Notation, it allows us to use data in this format.
import requests
from discord.ext import commands #Allows us to use commands such as ;;
from discord.ext.commands import has_permissions


API_KEY="trgE7X_ZmeZv"
PROJECT_TOKEN="tGJfm_DrRiSHtGJfm_DrRiSH"
RUN_TOEKN="tWbXT_53cBNJ"

class covid(commands.Cog):
	def __init__(self,client):
		self.client=client
	
	@commands.command()
	async def cases(self,ctx):
		response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
		data =json.loads(response.text)
		print(data)
		await ctx.send("no")

def setup(client):
	client.add_cog(covid(client))