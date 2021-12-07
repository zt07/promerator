import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
import DiscordUtils
import random

class music(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.Cog.listener() # this is a decorator for events/listeners
  async def on_ready(self):
  	print('readyyyy')
