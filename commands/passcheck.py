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

class passcheck(commands.Cog):
	def __init__(self,client):
		self.client=client

		
	@commands.command()
	async def passcheck(self,ctx,password):  #checks how secure a password is with a score rating.
		await ctx.message.delete()
		score=0
		password=str(password)	#makes password a string to work with
		if len(password)<4 or len(password)>12:
			embed=discord.Embed(tittle="Most websites wont except that length, try a password beetween 4 and 12 characters long.",color=green)
			await ctx.send(embed=embed)
		elif len(password)<5:
				score += 3
		elif len(password)<7:
			score += 5
	   
		for i in range(1, len(password)):
			if password[i] != password[0]:
				score-=1
		
		if password.isupper():
			score+=3
		elif password.islower():
			score-=1
		else: 
			for i in password:
				if i == ["@","$","!","#","%","^","&","*","(",")"]:
					score+=2
				if i==[1,2,3,4,5,6,7,8,9,10,0]:
					score+=1
				else: score+=0

def setup(client):
	client.add_cog(passcheck(client))
	