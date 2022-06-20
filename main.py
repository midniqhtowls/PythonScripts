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
token = "token"

bot.remove_command('help')

# Commands

@bot.command()
async def help(ctx):
  await ctx.send("loading help..")

bot.run(token)
