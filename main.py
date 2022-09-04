# Imports

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

# Variables 

version = "1.0.0"
prefix = "!"
username = "username"
status = "status"
token = "token"
delete_after = True # set this to false if you dont want the bot to delete its own message after 20 seconds

bot = commands.Bot(command_prefix=f"{prefix}", status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status}" , case_insensitive=True, intents=discord.Intents.all()))
bot.remove_command('help')

# Start up

@bot.event
async def on_ready():
    print(f"logged in as {bot.user} [{bot.user.id}]")
    print(f"prefix - {prefix}")
    print(f"version - {version}")
    print("------")

# Error Handlers
  
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        embed.add_field(name="**failed**",value="command not found", inline=False)
        embed.set_footer(text=f"{username} is currently at {version}")
        await ctx.message.delete()
        if delete_after == True:
            await ctx.send(embed=embed, delete_after=20.0)
        else:
            await ctx.send(embed=embed)

# Commands
  
@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"{prefix}help",value="shows the list of commands", inline=False)
    embed.add_field(name=f"{prefix}membercount",value="shows the server's member count", inline=False)
    embed.add_field(name=f"{prefix}embed",value="sends a embed with a title and a description", inline=False)
    embed.set_footer(text=f"{username} is currently at {version}")
    await ctx.message.delete()
    if delete_after == True:
        await ctx.send(embed=embed, delete_after=20.0)
    else:
        await ctx.send(embed=embed)

@bot.command()
async def membercount(ctx):
    embed = discord.Embed(color=0x2F3136)
    guild = ctx.guild
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"**membercount**",value=f"`{guild.member_count}` members", inline=False)
    embed.set_footer(text=f"{username} is currently at {version}")
    await ctx.message.delete()
    if delete_after == True:
        await ctx.send(embed=embed, delete_after=20.0)
    else:
        await ctx.send(embed=embed)

@bot.command()
async def embed(ctx, content, reason):
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(name=content,value=reason)
        embed.set_footer(text=f"{username} is currently at {version}")
        await ctx.message.delete()
        if delete_after == True:
            await ctx.send(embed=embed, delete_after=20.0)
        else:
            await ctx.send(embed=embed)

bot.run(token)
