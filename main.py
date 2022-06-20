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
username = "bot"
prefix = "!"
token = "OTY1OTY5Njg1Nzk3NTUyMTU4.GHlGnk.vS5HIH4rthIXfrRVsrQpy2y04egGpipGjAjAFs"

bot.remove_command('help')

# Commands

@bot.command()
async def help(ctx):
  await ctx.send("loading help..")
  
@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"**!help**",value="shows the current message", inline=False)
    embed.set_footer(text=f"{username} is currently at {version}")
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=20.0)

bot.run(token)
