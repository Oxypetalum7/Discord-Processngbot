import discord
import sys
from discord.ext import commands #コマンド関係　
import text_process
import run_sketch
import generate_gif
import shutil
import os


TOKEN = 'NjI1NTczOTYzNTAxNjY2MzE0.XrxStA.hnQIE7TsD16EYuLL5_xlqDoNgow'
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
        run_sketch.run_sketch()
        file_img = discord.File("sketch/out.gif")
        await message.channel.send('Here is a code result.', file=file_img)


#bot.run(TOKEN) #最後の行に記述
client.run(TOKEN)