import discord
from discord.ext import commands
from webserver import keep_alive

import os
client = commands.Bot(command_prefix = 'PREFIX GOES HERE')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Your Status'))

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run('BOT TOKEN GOES HERE ')
