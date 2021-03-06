import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
green = discord.Color.green()

class helpp(commands.Cog):
	def __init__(self,client):
		self.client=client


	@commands.command()
	async def help(self,ctx):
		embed = discord.Embed(title="Welcome to promerator", description="Here are the commands to use the bot. Make sure before each command to type ';;' Example: ;;help ", color=green)
		embed.add_field(name="clear", value="Deletes the amount of messages you specify limit is 500 messages. To use this type: clear 20(You can replace 20 with whatver number less then 500.)  (Only works if you have the Manage Messages role." , inline=False)
		embed.add_field(name="Source", value="Source code for this bot is shown here." , inline=False)
		embed.add_field(name="wiki_summary", value="Shows the first couple sentences of a Wikipedia article about your term, if nothing returns, it is likely that the term was not found as an article and try a similar word such as 'gaming' => 'video game' aliase wiki can be used.", inline=True)
		embed.add_field(name="help_contact", value="How you can contact me for any support." , inline=True)
		embed.add_field(name="search", value="Uses the WolframAplpha API to get the asnwer to your question that coem after. Example: ;;search popualation of Russia, or ;;search 5x+10=30" , inline=True)
		embed.add_field(name="ping_check", value="Check latency of the bot" , inline=True)
		embed.add_field(name="setprefix", value="Change the prefix that calls the bot." , inline=True)
		embed.add_field(name="eight_ball, coin flip", value="Flip a coin or use an 8 ball to determine your decisions! (That was a joke, the 8ball decisions are purely random.)" , inline=True)
		embed.add_field(name="quote", value="Returns a random quote." , inline=True)
		embed.add_field(name="run,code,evaL", value="executes code in Jdoodle API and sends back to user, . EX: ;;run python3 . print('hello World') supported languages include Python3, C and C++(GCC 11.1.0),Ruby,Go,Scala,csharp(mono 4.2.2), Swift,Rust 1.10.0, And all version 4 languages on https://docs.jdoodle.com/compiler-api/compiler-api. Please type ;;help_code for details" , inline=False)
		embed.add_field(name="latency",value=f'{round(self.client.latency * 1000)}ms')
		await ctx.send(embed=embed)

	@commands.command()
	async def ping_check(self,ctx):
		embed=discord.Embed(title="My ping is ",description=f'{round(self.client.latency * 1000)}ms',color=green)	
		await ctx.send(embed=embed)

	@commands.command()
	async def source(self,ctx):
		embed=discord.Embed(title="Source", url="https://github.com/zt07/ZT-s-Music", color=green)
		await ctx.send(embed=embed)

	@commands.command(breif="test command", description="test commanddesc")
	async def test(self,ctx):
		embed= discord.Embed(title=f"Check!", color = green)
		await ctx.send(embed=embed)
	
	@commands.command()
	async def help_contact(self,ctx):
		embed= discord.Embed(title=f"Help Contact:",descritpion="For any help you can dm me at zut0_7 on Instagram, or email me at zaheeb072@gmial.com", color = green)
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(helpp(client))