# Imports, DO NOT REMOVE OR CHANGE ANYTHING!

import discord
import asyncio
import random
import datetime
import time
from discord import user
from discord import message
from discord.activity import Game
from discord.user import User
from discord.ext import commands
from discord import guild
from discord.ext import tasks
from discord import mentions
from discord.ext.commands import Bot, has_permissions
from discord import Embed
from discord.utils import get

# Variables, DO NOT CHANGE THE NAME OF ANYTHING, PLEASE ONLY CHANGE THE THINGS INSIDE OF THE ""

version = "1.0.9" # not really important, just the footer of the embed and keeps track of the updates on the github, you'll have to keep checking the github for updates/bug fixes
lastestUpdate = "11/6/2023" # shows when the bot was last updated
prefix = "!" # sets the prefix, you can make it anything you want
username = "username" # for embed only, you will have to set the actual bot username in your discord developer application
status = "status" # sets the status, you can also make thing anything you want
status1 = "https://twitch.tv" # you dont have to fill this in if you are not using the streaming status
token = "token" # bots token, needed to run the bot
CaseInsensitive = True # if this is true, it will be case insensitive which means if the command name is "!help", you can run it by typing it the normal way or in all caps like "!HELP" or "!hElP, if you make it False, you wont be able to run it by typing "!hElP"
delete_after = True # set this to false if you dont want the bot to delete its own message after 20 seconds
delete_ownMessage = True # set this to false if you dont want the bot to delete your own message after running the command

# if you want to change the things below, read https://github.com/warcock/PythonScripts/blob/main/varInfo.py

bot = commands.Bot(
    command_prefix=f"{prefix}", 
    status=discord.Status.do_not_disturb,
    activity=discord.Streaming(name=f"{status}", url=f"{status1}"),
    case_insensitive=CaseInsensitive, 
    intents=discord.Intents.all()
)

bot.remove_command('help')


























































# DO NOT CHANGE ANYTHING UNDER HERE IF YOU DO NOT KNOW WHAT YOU ARE DOING!



































































































@bot.event
async def on_ready():
    print(f"logged in as {bot.user} [{bot.user.id}]")
    print(f"prefix - {prefix}")
    print(f"version - {version}")
    print("------")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        embed.add_field(name="**failed**",value="command not found", inline=False)
        embed.set_footer(text=f"{username} is currently at {version}")
        if delete_after and delete_ownMessage == True:
          await ctx.send(embed=embed, delete_after=20.0)
          await ctx.message.delete()
        elif delete_ownMessage == True:
          await ctx.send(embed=embed)
          await ctx.message.delete()
        elif delete_after == True:
          await ctx.send(embed=embed, delete_after=20.0)

@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"{prefix}help",value="shows the list of commands", inline=False)
    embed.add_field(name=f"{prefix}membercount",value="shows the server's member count", inline=False)
    embed.add_field(name=f"{prefix}embed",value="sends a embed with a title and a description", inline=False)
    embed.add_field(name=f"{prefix}botinfo",value="sends a embed with information of the bot", inline=False)
    embed.add_field(name=f"{prefix}invite",value="sends a embed with a link to invite the bot", inline=False)
    embed.add_field(name=f"{prefix}ping",value="sends a embed with the ping's latency", inline=False)
    embed.set_footer(text=f"{username} is currently at {version}")
    if delete_after and delete_ownMessage == True:
        await ctx.send(embed=embed, delete_after=20.0)
        await ctx.message.delete()
    elif delete_ownMessage == True:
        await ctx.send(embed=embed)
        await ctx.message.delete()
    elif delete_after == True:
        await ctx.send(embed=embed, delete_after=20.0)
@bot.command()
async def membercount(ctx):
    embed = discord.Embed(color=0x2F3136)
    guild = ctx.guild
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"**membercount**",value=f"`{guild.member_count}` members", inline=False)
    embed.set_footer(text=f"{username} is currently at {version}")
    if delete_after and delete_ownMessage == True:
        await ctx.send(embed=embed, delete_after=20.0)
        await ctx.message.delete()
    elif delete_ownMessage == True:
        await ctx.send(embed=embed)
        await ctx.message.delete()
    elif delete_after == True:
        await ctx.send(embed=embed, delete_after=20.0)

@bot.command()
async def embed(ctx, content, reason):
    embed = discord.Embed(color=0x2F3136)
    embed.add_field(name=content,value=reason)
    embed.set_footer(text=f"{username} is currently at {version}")
    if delete_after and delete_ownMessage == True:
        await ctx.send(embed=embed, delete_after=20.0)
        await ctx.message.delete()
    elif delete_ownMessage == True:
        await ctx.send(embed=embed)
        await ctx.message.delete()
    elif delete_after == True:
        await ctx.send(embed=embed, delete_after=20.0)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="**ping**",value=f"`{round(bot.latency * 1000)}ms`", inline=False)
    embed.set_footer(text=f"{username} is currently at {version}")
    if delete_after and delete_ownMessage == True:
      await ctx.send(embed=embed, delete_after=20.0)
      await ctx.message.delete()
    elif delete_ownMessage == True:
      await ctx.send(embed=embed)
      await ctx.message.delete()
    elif delete_after == True:
      await ctx.send(embed=embed, delete_after=20.0)

@bot.command()
async def invite(ctx):
  embed = discord.Embed(color=0x2F3136)
  embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
  embed.add_field(name="**invite**",value="[click here](https://discord.com/api/oauth2/authorize?client_id=847522533735847946&permissions=8&scope=bot)", inline=False)
  embed.set_footer(text=f"{username} is currently at {version}")
  if delete_after and delete_ownMessage == True:
    await ctx.send(embed=embed, delete_after=20.0)
    await ctx.message.delete()
  elif delete_ownMessage == True:
    await ctx.send(embed=embed)
    await ctx.message.delete()
  elif delete_after == True:
    await ctx.send(embed=embed, delete_after=20.0)

@bot.command()
async def botinfo(ctx):
  embed = discord.Embed(color=0x2F3136)
  embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
  embed.add_field(name="**info**",value=f"**{username}** is a bot made by **.warcock**. It is currently in **{len(bot.guilds)}** servers.", inline=False)
  embed.add_field(name="**updates**",value=f"This bot was last updated on **{lastestUpdate}**. It is currently in version **{version}**", inline=False)
  embed.set_footer(text=f"{username} is currently at {version}")
  if delete_after and delete_ownMessage == True:
    await ctx.send(embed=embed, delete_after=20.0)
    await ctx.message.delete()
  elif delete_ownMessage == True:
    await ctx.send(embed=embed)
    await ctx.message.delete()
  elif delete_after == True:
    await ctx.send(embed=embed, delete_after=20.0)

bot.run(token)
