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
'''
This code in documentation enough
'''
#jk

#Written by Zaheeb Tariq courtesy of the above libraries of course zaheeb07@gmail.com though response might take a while


music=DiscordUtils.Music()
client = discord.Client()
client = commands.Bot(command_prefix=';;', help_command=None)  #prefix is ;;, when a user wishes to address the bot, type in ;; then your command EX: ;;play.

green = discord.Color.green()# sort of a shortcut for code so instead of having to type out discord.Color.green() you can just say green. 


        
    

def grab_quote(): #defining a fuction here so we can just call or type out "grab_quote()" instead of what is below.
    response = requests.get(
        "https://zenquotes.io/api/random")  #get stuff from zenquotes api
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0][
        'a']  #quote is the data loaded previously
    return (quote)


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(';;help'))
  print(f' {client.user} is logged in and ready to RUMBLEEEE!!!!')
          #get exited when ready and set status

					


@client.command()
async def hi(ctx):
  await ctx.send("Whats up!")#responds with whats up whena  user types ;;hi


@client.command()
async def quote(ctx):
  embed=discord.Embed(title="Here you go!", description=grab_quote(),color=green)
  await ctx.send(embed=embed)


@client.command()
async def j(ctx):
    if ctx.author.voice is None:
        embed= discord.Embed(title="Failed :(", description=f"Get in a Voice Channel", color=green)
        await ctx.send(embed =embed)
    if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
    else:
        await ctx.ctx.author.voicechannel.moveto(ctx.author.voice.channel)


@client.command()
async def l(ctx): #leaves the vc it is in.
  await ctx.voice_client.disconnect()
  embed = discord.Embed(title=f"Stopped Playing!", description=f"I have left the voice channel", color=green) #Embedified
  await ctx.send(embed=embed)

@client.command()
async def p(ctx,*,url):
  player = music.get_player(guild_id=ctx.guild.id)
  if not player:
    player = music.create_player(ctx, ffmpeg_error_betterfix=True)
  if not ctx.voice_client.is_playing():
    await player.queue(url, search = True) #embedified 
    song = await player.play()
    embed = discord.Embed(title=f"Now playing!", description=f"{song.name}", color=green)
    await ctx.send(embed=embed) #plays a song from a url or just typin gin what you want to hear.
  else:
    song = await player.queue(url, search=True)
    embed = discord.Embed(title="Added to queue!", description=f"{song.name} Has been added.", color=green)
    await ctx.send(embed=embed) 

@client.command()
async def q(ctx):
  player = music.get_player(guild_id=ctx.guild.id)
  embed=discord.Embed(title="Current queue", 
  description=f"{', '.join([song.name for song in player.current_queue()])}", 
  color=green)
  await ctx.send(embed=embed)# displays the queue

@client.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping: #embedified
      embed=discord.Embed(title=f"Enabled loop!",description=f"loop has been enabled for {song.name}", color =green) 
      await ctx.send(embed=embed)
    else:#toggles on looping the song 
      embed=discord.Embed(title=f"Disabled loop!",description=f"loop has been Disabled for {song.name}", color =green) 
      await ctx.send(embed=embed)

@client.command()
async def pa(ctx):
    player = music.get_player(guild_id=ctx.guild.id)#pasues the music where it's at
    song = await player.pause()#embedded
    embed=discord.Embed(title="Paused!", description=f"{song.name} is now paused", color=green)
    await ctx.send(embed=embed)

@client.command()
async def r(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()#embedded
    embed=discord.Embed(title="Resumed", description=f"{song.name} is now playing!", color=green)
    await ctx.send(embed=embed)#resumes the audio

@client.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
      embed=discord.Embed(title="Skipped", description="Current song has been skipped!", color=green)
      await ctx.send(embed=embed)
    else:#skips your song
        embed=discord.Embed(title="Skipped", description="Current song has been skipped!", color=green)
        await ctx.send(embed=embed)
@client.command()
async def rem(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))#removes a song in queue
    embed=discord.Embed(title="Removed!", description=f"{song.name} has been removed from queue!", color=green)
    await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    if amount > 500:
        await ctx.send("You cant delete that many messages!")  #so it wont lag
    else:
        await ctx.channel.purge(limit=amount)  #clears messages
        embed=discord.Embed(title="Messages cleared!", description=f"{str(amount)} messages deleted!", color=green)
        await ctx.send(embed = embed)

@client.command()
async def randnum(ctx):

    
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel
							 
    embed1=discord.Embed(title="type a number you want to randomize from.", description="Must be the smaller number.", color=green) 
    await ctx.send(embed=embed1)
    msg1 = await client.wait_for("message", check=check)
    embed2=discord.Embed(title="Add your second number.", description="Must be greater then the previous number.", color=green) 
    await ctx.send(embed=embed2)
    msg2 = await client.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)
    if x < y:
        value = random.randint(x,y)
        embed3=discord.Embed(title="Your random number is...", description=f"{value}", color=green)
        await ctx.send(embed=embed3)
    else: embed4=discord.Embed(title="Failed", description="Please insure your first number is less then your second number", color=green) 
    
    await ctx.send(embed=embed4)


@client.command()
async def passcheck(ctx,password):  #checks how secure a password is with a score rating.
	await ctx.message.delete()
	score=0
	password=str(password)#makes password a string to work with
	if len(password)<4 or len(password)>12:
		embed=discord.Embed(tittle="Most websites wont except that length, try a password beetween 4 and 12 characters long.",color=green)
		await ctx.send(emebd=embed)
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
	
	
	
	embed=discord.Embed(tittle="Your password score rating is...",description=f"Your password score is {score}",color=green)
	await ctx.send(embed=embed)




'''
pip install py-cord
pip install DiscordUtils[voice]
run = """
pip install py-cord
pip install DiscordUtils[voice]
pip install bython
python main.py
"""
'''
client.load_extension("commands.helpp")
client.load_extension("commands.music")


keepAlive()
my_secret = os.environ['TOKEN']

client.run(os.getenv('TOKEN'))
