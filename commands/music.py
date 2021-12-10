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

music=DiscordUtils.Music()
green = discord.Color.green()

class music(commands.Cog):
	def __init__(self,client):
		self.client=client

	@commands.command()
	async def j(self,ctx):
		if ctx.author.voice is None:
			embed= discord.Embed(title="Failed :(", description=f"Get in a Voice Channel", color=green)
			await ctx.send(embed =embed)
			if ctx.voice_client is None:
				await ctx.author.voice.channel.connect()
			else:
				await ctx.ctx.author.voicechannel.moveto(ctx.author.voice.channel)


@commands.command()
async def l(self,ctx): #leaves the vc it is in.
  await ctx.voice_client.disconnect()
  embed = discord.Embed(title=f"Stopped Playing!", description=f"I have left the voice channel", color=green) #Embedified
  await ctx.send(embed=embed)

@commands.command()
async def p(self,ctx,*,url):
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

@commands.command()
async def q(self,ctx):
  player = music.get_player(guild_id=ctx.guild.id)
  embed=discord.Embed(title="Current queue", 
  description=f"{', '.join([song.name for song in player.current_queue()])}", 
  color=green)
  await ctx.send(embed=embed)# displays the queue

@commands.command()
async def loop(self,ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping: #embedified
      embed=discord.Embed(title=f"Enabled loop!",description=f"loop has been enabled for {song.name}", color =green) 
      await ctx.send(embed=embed)
    else:#toggles on looping the song 
      embed=discord.Embed(title=f"Disabled loop!",description=f"loop has been Disabled for {song.name}", color =green) 
      await ctx.send(embed=embed)

@commands.command()
async def pa(self,ctx):
    player = music.get_player(guild_id=ctx.guild.id)#pasues the music where it's at
    song = await player.pause()#embedded
    embed=discord.Embed(title="Paused!", description=f"{song.name} is now paused", color=green)
    await ctx.send(embed=embed)

@commands.command()
async def r(self,ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()#embedded
    embed=discord.Embed(title="Resumed", description=f"{song.name} is now playing!", color=green)
    await ctx.send(embed=embed)#resumes the audio

@commands.command()
async def skip(self,ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
      embed=discord.Embed(title="Skipped", description="Current song has been skipped!", color=green)
      await ctx.send(embed=embed)
    else:#skips your song
        embed=discord.Embed(title="Skipped", description="Current song has been skipped!", color=green)
        await ctx.send(embed=embed)
@commands.command()
async def rem(self,ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))#removes a song in queue
    embed=discord.Embed(title="Removed!", description=f"{song.name} has been removed from queue!", color=green)
    await ctx.send(embed = embed)


def setup(client):
    client.add_cog(music(client))


