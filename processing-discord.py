import os
import shutil
import sys
import configparser

import discord
from discord.ext import commands  # コマンド関係

import generate_gif
import run_sketch
import text_process

config = configparser.ConfigParser()
config.read('./config.ini')
TOKEN = config['TOKEN']['token']
client = discord.Client()

@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
    if message.content.startswith('!SHUTDOWN_BOT'):
        await message.channel.send('See You')
        client.logout()
        sys.exit()
    elif message.content.startswith('!processing'):
        await message.channel.send(message.author.mention + ' running...')
        code = message.content
        text_process.writecontent(code)
        try:
          run_sketch.run_sketch()
          generate_gif.generate_image()
          file_img = discord.File("sketch/out.gif")
          await message.channel.send('Here is a code result.', file=file_img)
        except:
          await message.channel.send('GIF generation Filed')


client.run(TOKEN)
