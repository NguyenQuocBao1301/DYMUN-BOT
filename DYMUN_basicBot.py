# This bot is created in 2024 at DYMUN 2024. The code can be manipulated all how you want.
# DYMUN is a MUN conference based in Danang city, Vietnam.
# It is our pleasure to contribute a little bit to your conference's success.

import discord
from discord.ext import commands
import time


intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents=intents)

cd_id = #Id of the channel which all the proposed directives are sent into
granted_id = #Id of the channel which all the granted directives and press releases are sent to
press_id = #Id of the channel which all the proposed press releases are sent into

message_origin = {}
last_directive_time = {}
maxTime = 120 #2 phut
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    cd_channel = bot.get_channel(cd_id)
    press_channel = bot.get_channel(press_id)
  
    if message.author == bot.user:
      return

    if message.content.startswith('/directive'):
      user_id = message.author.id
      current_time = time.time()
      if user_id in last_directive_time:
          elapsed_time = current_time - last_directive_time[user_id]
          if elapsed_time < maxTime:  
              await message.channel.send(f"{message.author.mention}, you must wait {int(maxTime - elapsed_time)} more seconds before you can send another directive. Time limit is 2 minutes.")
              await message.delete()
              return
      last_directive_time[user_id] = current_time

      return_msg = str(message.author.display_name)+' - Directive - '+message.content.replace('/directive', '')
      sent_message = await cd_channel.send(return_msg)
      reactions = ['✅', '❌', '❓']
      for reaction in reactions:
        await sent_message.add_reaction(reaction)
      message_origin[sent_message.id] = (message.channel.id, message.id)
    if message.content.startswith('/jointDirective'):
      user_id = message.author.id
      current_time = time.time()
      if user_id in last_directive_time:
          elapsed_time = current_time - last_directive_time[user_id]
          if elapsed_time < maxTime:
              await message.channel.send(f"{message.author.mention}, you must wait {int(maxTime - elapsed_time)} more seconds before you can send another directive. Time limit is 2 minutes.")
              await message.delete()
              return
      last_directive_time[user_id] = current_time


      return_msg = str(message.author.display_name)+' - Joint Directive - ' + message.content.replace('/jointDirective', '')
      sent_message = await cd_channel.send(return_msg)
      reactions = ['✅', '❌', '❓']
      for reaction in reactions:
        await sent_message.add_reaction(reaction)
      message_origin[sent_message.id] = (message.channel.id, message.id)
      sent_message = await cd_channel.send(return_msg)
    if message.content.startswith('/openChannel'):
      return_msg = str(message.author.mention)+' wants to open a channel with '+ message.content.replace('/openChannel', '')
      sent_message = await cd_channel.send(return_msg)
    if message.content.startswith('/PR'):
      return_msg = str(message.author.display_name)+' - PressRelease - '+message.content.replace('/PR', '')
      sent_message = await press_channel.send(return_msg)
      reactions = ['✅', '❌', '❓']
      for reaction in reactions:
        await sent_message.add_reaction(reaction)
      message_origin[sent_message.id] = (message.channel.id, message.id)
      
      
    await bot.process_commands(message)  # Ensure commands are processed
  
@bot.command(name='poll')
async def poll(ctx):
  message = await ctx.send('React with your choice: Yes, No, or ?')
  reactions = ['✅', '❌', '❓']

  for reaction in reactions:
    await message.add_reaction(reaction)

@bot.event
async def on_reaction_add(reaction, user):
  if user == bot.user:
    return

  original_channel_id, _ = message_origin.get(reaction.message.id, (None, None))
  emoji = reaction.emoji
  if emoji == '✅':
      response = 'Granted'
      granted_directive = bot.get_channel(granted_id)
      await granted_directive.send(reaction.message.content)

  elif emoji == '❌':
      response = 'Not Granted'
  elif emoji == '❓':
      response = 'Detail out'
  else:
      return
  
  if original_channel_id:
      original_channel = bot.get_channel(original_channel_id)
      if original_channel:
          await original_channel.send(f'{response}')

bot.run("TOKEN OF YOUR BOT")