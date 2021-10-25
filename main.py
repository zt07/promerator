import discord
import asyncio
import os
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
import DiscordUtils
#Written by Zaheeb Tariq courtesy of the above libraries of course zaheeb07@gmail.com though response might take a while

music=DiscordUtils.Music()
client = discord.Client()
client = commands.Bot(command_prefix=';;',help_command=None)  #prefix is ;;, when a user wishes to address the bot, type in ;; then your command EX: ;;play.

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
    print(f' {client.user} is logged in and ready to RUMBLEEEE!!!!'
          )  #get exited when ready

@client.command()
async def ping(ctx):
  await ctx.send("no")
 #only a test command      

@client.command()
async def help(ctx):
  embed = discord.Embed(title="Welcome to ZT's Music!",
   description="Here is a list of commands to guide you. ",
   color=green)
  await ctx.send(embed=embed)


@client.command(breif="test command", description="test commanddesc")
async def test(ctx):
  await ctx.send("Check!")

@client.command()
async def hi(ctx):
  await ctx.send("Whats up!")#responds with whats up whena  user types ;;hi


@client.command()
async def quote(ctx):
    await ctx.send(grab_quote())


@client.command()
async def j(ctx):
    if ctx.author.voice is None:
        await ctx.send("get in a voice channel first")
    if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
    else:
        await ctx.ctx.author.voicechannel.moveto(ctx.author.voice.channel)


@client.command()
async def l(ctx): #leaves the vc it is in.
  await ctx.voice_client.disconnect()
  await ctx.send("goodbye!")

@client.command()
async def p(ctx,*,url):
  player = music.get_player(guild_id=ctx.guild.id)
  if not player:
    player = music.create_player(ctx, ffmpeg_error_betterfix=True)
  if not ctx.voice_client.is_playing():
    await player.queue(url, search = True)
    song = await player.play()
    await ctx.send(f"Playing {song.name}") #plays a song from a url or just typin gin what you want to hear.
  else:
    song = await player.queue(url, search=True)
    await ctx.send(f"{song.name} added to queue")

@client.command()
async def q(ctx):
  player = music.get_player(guild_id=ctx.guild.id)
  await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")# displays the queue

@client.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")

@client.command()
async def pa(ctx):
    player = music.get_player(guild_id=ctx.guild.id)#pasues the music where it's at
    song = await player.pause()
    await ctx.send(f"{song.name} paused!")

@client.command()
async def res(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"{song.name} playing!")#resumes the audio

@client.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")
@client.command()
async def rem(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    if amount > 500:
        await ctx.send("You cant delete that many messages!")  #so it wont lag
    else:
        await ctx.channel.purge(limit=amount)  #clears messages
        await ctx.send(str(amount) + " messages deleted!")


@client.command()
async def embed(ctx):
    embed = discord.Embed(title="command sent",
                          description="done",
                          color=discord.Color.green())
    await ctx.send(embed=embed) # trying to learn embeds











my_secret = os.environ['TOKEN']

client.run(os.getenv('TOKEN'))
