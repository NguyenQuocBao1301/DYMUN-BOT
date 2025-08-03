# This discord bot served DYMUN'25 (Danang Youth Model United Nations) Crisis Coucil UNOOSA/UNSC for the year 2025.
# It is a crisis council bot that allows users to send directives, joint directives, connect requests, research requests, and press releases.
# Also allows Crisis Directors to manage country data such as budget, satellites, and ASAT weapons.
# To initiate countries with data, use printCountries.py to generate the countries dictionary with the output from the log file. Remember to use it before any time the bot is run.
import discord
from discord.ext import commands, tasks
import time
import os

class Country:
    def __init__(self, name, budget, earth_sat, mars_sat, asat_weapons):
        self.name = name
        self.budget = budget
        self.earth_sat = earth_sat
        self.mars_sat = mars_sat
        self.asat_weapons = asat_weapons

    def _status_label(self, value):
        return {
            0: "Non-existent",
            1: "Developing",
            2: "Available",
            3: "Operating"
        }.get(value, f"Unknown ({value})")

    def info(self):
        return (
            f"{self.name} | Budget: ${self.budget:_} | "
            f"Earth Orbit Satellites: {self._status_label(self.earth_sat)} | "
            f"Mars Orbit Satellites: {self._status_label(self.mars_sat)} | "
            f"ASAT Weapons: {self._status_label(self.asat_weapons)}"
        )
    
    def printCountry(self):
        return (f"{self.name} {self.budget:_} {self.earth_sat} {self.mars_sat} {self.asat_weapons}")

countries = {
    "pk": Country("Pakistan", 1_150_000_000, 3, 0, 0),
    "jp": Country("Japan", 13_100_000_000, 0, 3, 0),
    "ca": Country("Canada", 12_999_000_000, 3, 3, 0),
    "fr": Country("France", 29_000_000_000, 3, 0, 3),
    "ru": Country("Russia", 27_880_000_000, 2, 0, 2),
    "us": Country("United States", 289_490_000_000, 3, 2, 3),
    "cn": Country("China", 98_050_000_000, 2, 3, 2),
    "in": Country("India", 67_500_000_000, 2, 0, 0),
    "de": Country("Germany", 18_614_500_000, 2, 3, 3),
    "it": Country("Italy", 26_490_000_000, 2, 0, 0),
    "kp": Country("North Korea", 4_736_000_000, 0, 0, 0),
    "ir": Country("Iran", 30_950_000_000, 2, 0, 1),
    "test": Country("Testland", 100_000_000, 1, 0, 0),
}
user_country_mapping = {
    # example user ID mappings (you can replace with real user IDs)
    : "pk",
    : "jp",
    : "ca",
    : "fr",
    : "ru",
    : "us", 
    : "cn",
    : "in",
    : "de", 
    : "it",
    : "kp",
    : "ir",
    : "test"  # Example test user
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

directive_id =   # Replace with actual channel ID for directives
granted_dir_id =   # Replace with actual channel ID for granted directives
press_id =  # Replace with actual channel ID for press releases Duoc granted vao cung cho voi granted_dir_id
connect_id =   # Replace with actual channel ID for connect requests
research_id =  # Replace with actual channel ID for research requests
general_id =   # Replace with actual channel ID for general messages

message_origin = {}
last_directive_time = {}
maxTime = 300  # 5 minutes in seconds

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    update_file.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('/dir'):
        user_id = message.author.id
        current_time = time.time()
        if user_id in last_directive_time:
            elapsed = current_time - last_directive_time[user_id]
            if elapsed < maxTime:
                await message.channel.send(f"{message.author.mention}, wait {int(maxTime - elapsed)} seconds before sending another directive.")
                return

        last_directive_time[user_id] = current_time

        cd_channel = bot.get_channel(directive_id)
        return_msg = f"{message.author.display_name} - Directive - {message.content.replace('/dir', '').strip()}"
        sent_msg = await cd_channel.send(return_msg)
        for emoji in ['✅', '❌', '❓']:
            await sent_msg.add_reaction(emoji)
        message_origin[sent_msg.id] = (message.channel.id, message.id)
    
    if message.content.startswith('/jdir'):
      user_id = message.author.id
      current_time = time.time()
      if user_id in last_directive_time:
          elapsed_time = current_time - last_directive_time[user_id]
          if elapsed_time < maxTime:
              await message.channel.send(f"{message.author.mention}, you must wait {int(maxTime - elapsed_time)} more seconds before you can send another directive. Time limit is 4 minutes.")
              await message.delete()
              return
      last_directive_time[user_id] = current_time

      cd_channel = bot.get_channel(directive_id)
      return_msg = str(message.author.display_name)+' - Joint Directive - ' + message.content.replace('/jdir', '')
      sent_message = await cd_channel.send(return_msg)
      reactions = ['✅', '❌', '❓']
      for reaction in reactions:
        await sent_message.add_reaction(reaction)
      message_origin[sent_message.id] = (message.channel.id, message.id)
      #sent_message = await cd_channel.send(return_msg)
    if message.content.startswith('/connect'):
      connect_channel = bot.get_channel(connect_id)
      return_msg = str(message.author.mention)+' wants to open a channel with '+ message.content.replace('/connect', '')
      sent_message = await connect_channel.send(return_msg)
    if message.content.startswith('/research'):
        research_channel = bot.get_channel(research_id)
        return_msg = str(message.author.mention)+' '+ message.content.replace('/research', '')
        sent_message = await research_channel.send(return_msg)
    if message.content.startswith('/pr'):
      return_msg = str(message.author.display_name)+' - PressRelease - '+message.content.replace('/pr', '')
      sent_message = await bot.get_channel(press_id).send(return_msg)
      reactions = ['✅', '❌', '❓']
      for reaction in reactions:
        await sent_message.add_reaction(reaction)
      message_origin[sent_message.id] = (message.channel.id, message.id)


    if message.content.startswith('/info'):
        user_id = message.author.id
        if user_id in user_country_mapping:
            code = user_country_mapping[user_id]
            country = countries[code]
            await message.channel.send(country.info())
    
    if message.content.startswith('/budget'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          added_money = int(float(message.content.split(" ")[2]))
          country.budget += added_money
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Old Budget {country.budget-added_money} Budget: {country.budget}")
    
    if message.content.startswith('/set1'):
       country_name = message.content.split(" ")[1].lower()
       if country_name in countries:
           country = countries[country_name]
           country.earth_sat = int(message.content.split(" ")[2])
           user_id = message.author.id
           await message.channel.send(f"{country_name} - Earth Orbit Satellites set to {country.earth_sat}")
    if message.content.startswith('/set2'):
         country_name = message.content.split(" ")[1].lower()
         if country_name in countries:
              country = countries[country_name]
              country.mars_sat = int(message.content.split(" ")[2])
              user_id = message.author.id
              await message.channel.send(f"{country_name} - Mars Orbit Satellites set to {country.mars_sat}")
    if message.content.startswith('/set3'):
        country_name = message.content.split(" ")[1].lower()
        if country_name in countries:
            country = countries[country_name]
            country.asat_weapons = int(message.content.split(" ")[2])
            user_id = message.author.id
            await message.channel.send(f"{country_name} - ASAT Weapons set to {country.asat_weapons}")
    
    if message.content.startswith('/printcountry'):
        output = "```"
        for country in countries.values():
            output += country.info() + "\n"
        output += "```"
        await message.channel.send(output)
    if message.content.startswith('/botsays'):
        general_channel = bot.get_channel(general_id)
        return_msg = message.content.replace('/botsays', '')
        sent_message = await general_channel.send(return_msg)

    await bot.process_commands(message)

    

@bot.event
async def on_reaction_add(reaction, user):
  if user == bot.user:
    return

  original_channel_id, _ = message_origin.get(reaction.message.id, (None, None))
  emoji = reaction.emoji
  if emoji == '✅':
      response = 'Granted'
      granted_directive = bot.get_channel(granted_dir_id)
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

@tasks.loop(seconds=30)
async def update_file():
    os.makedirs("log", exist_ok=True)
    currenttime = time.time()
    fileName = f"log/country_data_{int(currenttime)}.txt"
    with open(fileName, "w") as f:
        for c in countries.values():
            f.write(c.printCountry() + "\n")

bot.run("your token here")
