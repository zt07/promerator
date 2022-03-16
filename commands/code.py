import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
green = discord.Color.green()
'''
Write and execute code in Python using discord
'''

c_ID = os.environ['Jdoodle_clientID']#cleint an dsecret id used for Jdoodle API
c_SECRET = os.environ['Jdoodle_ClientSecret']
endpoint="https://api.jdoodle.com/execute"#where request gets sent to
#An HTTP Post request is made with the code to be executed, then the website returns data in JSON format of the executed code. WHich is returned to the user in Discord.
class eval(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command(aliases=['PY',"Python"])
	async def py(self, ctx,*, stdin,codee,):
		if "```py" in codee:
			codee=codee[5:-3]
		global data
		
		data ={
   	"script" : f'{codee}',#send scode parameter in the request
   	"language": 'python3',
		"versionIndex": '3',
		"stdin": f'{stdin}',
   	"clientId": c_ID,
   	"clientSecret": c_SECRET
			}
		header={'content-type': 'application/json'}
		
		r=requests.post(url=endpoint, json=data, headers=header)#creates request to that
		embed=discord.Embed(title=f"Your request has returned with status code {r.json()['statusCode']}",description=f"``` {r.json()['output']} ```",color=green)#embed
		embed.add_field(name="latency",value=f'{round(self.client.latency * 1000)}ms')#returns latency
		await ctx.send(embed=embed)

	@commands.command(aliases=["C"])
	async def c(self, ctx,stdin,type,*, codee):
		if "```c" in codee:
			codee=codee[4:-3]
		global data
		
		data ={
   	"script" : f'{codee}',#send scode parameter in the request
   	"language": 'c',
		"versionIndex": '0',
		"stdin": f'{stdin}',
   	"clientId": c_ID,
   	"clientSecret": c_SECRET
			}
		header={'content-type': 'application/json'}
		
		r=requests.post(url=endpoint, json=data, headers=header)#creates request to that
		embed=discord.Embed(title=f"Your request has returned with status code {r.json()['statusCode']}",description=f"``` {r.json()['output']} ```",color=green)#embed
		embed.add_field(name="latency",value=f'{round(self.client.latency * 1000)}ms')#returns latency
		await ctx.send(embed=embed)
def setup(client):#cog creation
	client.add_cog(eval(client))