import discord
import os
import json
import requests
from discord.ext import commands


client = discord.Client()
client = commands.Bot(command_prefix = ';;')#prefix is ;;

def grab_quote():
  response = requests.get("https://zenquotes.io/api/random") #get stuff from zenquotes api
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a'] #quote is the data loaded previously
  return(quote) 


@client.event
async def on_ready():
    print(f' {client.user} is logged in and ready to RUMBLEEEE!!!!' ) #get exited when ready
    
@client.event
async def on_message(message):
    if message.author == client.user:# dont respond to our selves
        return


@client.command()
async def hi(ctx):
  await ctx.send("hey!")
@client.command()
async def quote(ctx):
  await ctx.send(grab_quote())

#@client.command()
#async def clear(ctx, amount=10):
  #await ctx.channel.purge(list=amount)#clears messages
 

    
     
     
   
        
my_secret = os.environ['TOKEN']



client.run(os.getenv('TOKEN'))

