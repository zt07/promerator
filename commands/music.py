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

class music(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command()
	async def cock(self, ctx):
		await ctx.send("literally in one")

def setup(bot):
    bot.add_cog(music(bot))


