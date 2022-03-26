import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
green = discord.Color.green()
'''
Write and execute code in Python using discord
'''

c_ID = os.getenv('Jdoodle_clientID')  #clint an dsecret id used for Jdoodle API
c_SECRET = os.getenv('Jdoodle_ClientSecret')
endpoint = "https://api.jdoodle.com/execute"  #where request gets sent to

#An HTTP Post request is made with the code to be executed, then the website returns data in JSON format of the executed code. WHich is returned to the user in Discord.
class eval(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['eval', "code"])
    async def run(self,ctx,lang,stdin,*,codee,):
        if "```cpp" in codee:
            codee = codee[6:-3]#Code blocks adds extra charcters what mess with the code sent to the API.
        if "```c" in codee:			#Extra charcters being removed here.
            codee = codee[4:-3]
        if "```py" in codee:
            codee = codee[5:-3]
        global data
        version = '4'# Version 4 of each language by default
        if lang == 'c' or lang == 'cpp':
            version = '5'
        data = {
            "script": f'{codee}',  #send scode parameter in the request
            "language": f'{lang}', #Our programming language chosen from the command
            "versionIndex": f'{version}', 			# data is all the JSON data we want to send to Jdoodle API
            "stdin": f'{stdin}', #ANy console input that may be re
            "clientId": c_ID,
            "clientSecret": c_SECRET
        }
        print(data)
        header = {'content-type': 'application/json'}
				
        r = requests.post(url=endpoint, json=data, headers=header)
        print(r)
		
        embed = discord.Embed(title=f"Your request has returned with status code {r.json()['statusCode']}",description=f"``` {r.json()['output']} ```",color=green)  												#embedembed.add_field(name="latency",value=f'{round(self.client.latency * 1000)}ms')  #returns latency
        await ctx.send(embed=embed)


def setup(client):  #cog creation
    client.add_cog(eval(client))
