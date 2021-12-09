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

class helpp(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command()
	async def help(self,ctx):
		embed = discord.Embed(title="Welcome to ZT's Music!", description="Here are the commands to use the bot. Make sure before each command to type ';;' Example: ;;j ", color=green)
		embed.add_field(name="j (Join)", value="Joins the voice channel you are in (You must use this before the P command or it wont work)", inline=True)
		embed.add_field(name="p (play)", value="plays whatever music you selected, make sure you put in a search term such as 'Nyan Cat' or paste in the exact link.", inline=True)
		embed.add_field(name="hi", value="Responds with Whats up!" , inline=True)
		embed.add_field(name="quote", value="Responds with a cool quote." , inline=True)
		embed.add_field(name="test", value="Will stay while the bot is in development" , inline=True)
		embed.add_field(name="l (Leave)", value="Ends the music and leaves your voice channel" , inline=True)
		embed.add_field(name="q (Queue)", value="Shows you the list of songs queued up" , inline=True)
		embed.add_field(name="rem", value="Remove a song from he queue For it to work you have to put a number that corrsponds with its place in queue For example: song1, song2, song3, song4, If you wish to remove song 1 then type ;;rem 0 or for song 1 type rem 2,for song2 type rem 3 and so on. ", inline=False)
		embed.add_field(name="loop", value="Puts the current song on repeat, use the command agian to disable" , inline=True)
		embed.add_field(name="pa", value="Pauses the song in its current place" , inline=True)
		embed.add_field(name="r", value="Resumes the song after you pause it." , inline=True)
		embed.add_field(name="skip", value="Skips the song and goes tot he next one in queue" , inline=True)
		embed.add_field(name="Source", value="Source code for this bot is shown here." , inline=True)
		embed.add_field(name="clear", value="Deletes the amount of messages you specify limit is 500 messages. To use this type: clear 20(You can replace 20 with whatver number less then 500.)  (Only works if you have the Manage Messages role." , inline=False)
		embed.add_field(name="Source", value="Source code for this bot is shown here." , inline=False)
		await ctx.send(embed=embed)

	@commands.command()
	async def source(self,ctx):
		embed=discord.Embed(title="Source", url="https://github.com/zt07/ZT-s-Music", color=green)
		await ctx.send(embed=embed)

	@commands.command(breif="test command", description="test commanddesc")
	async def test(self,ctx):
		embed= discord.Embed(title=f"Check!", color = green)
		await ctx.send(embed=embed)


def setup(client):
	client.add_cog(helpp(client))