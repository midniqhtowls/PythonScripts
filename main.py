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
  
@bot.command()
async def Hi(ctx):
  await ctx.send("Hi!")

version = "1.0.0"
username = "bot"
prefix = "!"
token = "OTY1OTY5Njg1Nzk3NTUyMTU4.GgBiFf.6XuM_MP9OtQ7qXjhyN79kLK-cyV0pKxDpT3djQ"
