import discord
import os
import json
import requests


client = discord.Client()

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

    if message.content == (';;help'):
        await message.channel.send('I can play music from Youtube and send you a quote if you want, You can address me with ;;')
    
    if message.content == (";;quote"):
      await message.channel.send(grab_quote()) #calling grab quote function for a quote
    
    if message.content == ("hello"):
       await message.channel.send("Whats up!") 
    if message.content == ("Hello"):
       await message.channel.send("Whats up!") 


    
     
     
   
        
my_secret = os.environ['TOKEN']



client.run(os.getenv('TOKEN'))

