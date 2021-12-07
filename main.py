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
async def ping(ctx):
  await ctx.send("no")
 #only a test command      

@client.command()
async def help(ctx):
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
@client.command()
async def source(ctx):
    embed=discord.Embed(title="Source", url="https://github.com/zt07/ZT-s-Music", color=green)
    await ctx.send(embed=embed)

@client.command(breif="test command", description="test commanddesc")
async def test(ctx):
  embed= discord.Embed(title=f"Check!", color = green)
  await ctx.send(embed=embed)

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

@client.commands()
async def cogt(ctx,extension):
	client.load_extension(f'cogs.{extension}')


'''
pip install py-cord
pip install DiscordUtils[voice]
run = """
pip install py-cord
pip install DiscordUtils[voice]
python main.py
"""
'''

keepAlive()
my_secret = os.environ['TOKEN']

client.run(os.getenv('TOKEN'))
