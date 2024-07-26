# This bot is created in 2024 at DYMUN 2024. The code can be manipulated all how you want.
# DYMUN is a MUN conference based in Danang city, Vietnam.
# It is our pleasure to contribute a little bit to your conference's success.
import discord
from discord.ext import commands, tasks
import time

class Country:
  def __init__(self, name, troop, s0, s1, s2, s3, budget, aircraft, ship, car):
      self.name = name
      self.troop = troop
      self.s0 = s0
      self.s1 = s1
      self.s2 = s2
      self.s3 = s3
      self.budget = budget
      self.aircraft = aircraft
      self.ship = ship
      self.car = car

  def info(self):
      return (f"{self.name} - Troops: {self.troop}, Budget: {self.budget}, Aircrafts: {self.aircraft}, Ships: {self.ship}, Cars: {self.car}")
  def country(self):
      return (f"{self.name} - Troops: {self.troop}, Budget: {self.budget}, Aircrafts: {self.aircraft}, Ships: {self.ship}, Cars: {self.car}, s0: {self.s0}, s1: {self.s1}, s2: {self.s2}, s3: {self.s3}")
countries = {
                                        
    "ru": Country("Russian Federation", 6350000, 0, 0, 0, 0, 5708000000, 5, 6, 100000),
    "uk": Country("United Kingdom", 2040000, 0, 0, 0, 0, 39215000000, 0, 0, 0),
    "af": Country("Islamic Republic of Afghanistan", 20000, 0, 0, 0, 0, 75000000, 0, 0, 3000),
    "us": Country("United States of America", 1165000, 0, 0, 0, 0, 270954000000, 60, 70, 100000),
    "fr": Country("French Republic", 243000, 0, 0, 0, 0, 7941000000, 10, 50, 1000),
    "bf": Country("People’s Republic of Burkina Faso", 7000, 0, 0, 0, 0, 34965000, 0, 0, 50),
    "sy": Country("Syrian Arab Republic", 247600, 0, 0, 0, 0, 241860000, 1, 1, 20014),
    "ye": Country("Republic of Yemen", 66700, 0, 0, 0, 0, 540000000, 0, 0, 0),
    "ml": Country("Republic of Mali", 90000, 0, 0, 0, 0, 140325000, 0, 0, 0),
    "cn": Country("People’s Republic of China", 2250000, 0, 0, 0, 0, 26561000000, 0, 0, 0),
    "iq": Country("Republic of Iraq", 414500, 0, 0, 0, 0, 558975000, 0, 1, 110),
    "ir": Country("The Islamic Republic of Iran", 420000, 0, 0, 0, 0, 8527940000, 2, 3, 3),
    "mx": Country("United Mexican States", 174550, 0, 0, 0, 0, 3027980000, 2, 0, 100),
    "de": Country("Federal Republic of Germany", 10197000, 89800, 0, 0, 0, 15112400000, 5, 6, 50),
    "pk": Country("The Islamic Republic of Pakistan", 517000, 0, 0, 0, 0, 1435600000, 2, 0, 1000),
    "test": Country("Test", 123, 0, 0, 0, 0, 123, 0, 0, 0)
}

user_country_mapping = {
    589997555212091414: "ru",
    919944210520608818: "uk", 
    1128898275144105984: "af",
    263593574812090368: "us",
    1263341151474421794: "fr",
    760856163142074399: "bf",
    1263101065562161152: "sy",
    930309796945596507: "ye",
    911139647260860456: "ml",
    752149695391989890: "cn",
    942999481673203722: "iq",
    1031008186012012614: "ir",
    907995976336310292: "mx",
    893010168630083584: "de",
    1263357883702313093: "pk",
    950190865983344651: "test"
}

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents=intents)

cd_id = 1263097333160083540
granted_id = 1263141526943563817
press_id = 1263350807659810940 #cd
PR_id = 1263355647311745024

aircraft_price = 500000000
ship_price = 300000000
car_price = 10000
s0_price = 20
s1_price = 70
s2_price = 140
s3_price = 300

message_origin = {}
last_directive_time = {}
maxTime = 210 #3.5 phut
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    update_file.start()

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
              await message.channel.send(f"{message.author.mention}, you must wait {int(maxTime - elapsed_time)} more seconds before you can send another directive. Time limit is 3.5 minutes.")
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
              await message.channel.send(f"{message.author.mention}, you must wait {int(maxTime - elapsed_time)} more seconds before you can send another directive. Time limit is 3.5 minutes.")
              await message.delete()
              return
      last_directive_time[user_id] = current_time


      return_msg = str(message.author.display_name)+' - Joint Directive - ' + message.content.replace('/jointDirective', '')
      sent_message = await cd_channel.send(return_msg)
      reactions = ['✅', '❌', '❓']
      for reaction in reactions:
        await sent_message.add_reaction(reaction)
      message_origin[sent_message.id] = (message.channel.id, message.id)
      #sent_message = await cd_channel.send(return_msg)
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
    if message.content.startswith('/info'):
      user_id = message.author.id
      if user_id in user_country_mapping:
          country_name = user_country_mapping[user_id]
          country = countries[country_name]
          await message.channel.send(country.info())
    if message.content.startswith('/country'):
      user_id = message.author.id
      if user_id in user_country_mapping:
          country_name = user_country_mapping[user_id]
          country = countries[country_name]
          await message.channel.send(country.country())
    if message.content.startswith('/troop'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.troop += int(message.content.split(" ")[2])
          country.budget -= 50*int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Army: {country.troop}")
    if message.content.startswith('/addtroop'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.troop += int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Army: {country.troop}")
    if message.content.startswith('/addair'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.aircraft += int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Aircraft: {country.aircraft}")
    if message.content.startswith('/addship'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.ship += int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Ships: {country.ship}")
    if message.content.startswith('/addcar'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.car += int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Cars: {country.car}")
    if message.content.startswith('/adds0'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.s0 += int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - s0: {country.s0}")
    if message.content.startswith('/adds1'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.s1 += int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - s1: {country.s1}")
    if message.content.startswith('/adds2'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.s2 += int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - s2: {country.s2}")
    if message.content.startswith('/adds3'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.s3 += int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - s3: {country.s3}")
    if message.content.startswith('/s0'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.s0 += int(0.9*int(message.content.split(" ")[2]))
          country.troop -= int(message.content.split(" ")[2])
          country.budget -= s0_price*int(message.content.split(" ")[2])
          if country.budget < 0 or country.troop < 0:
            await message.channel.send("Violation, not enough budget or not enough troop")
            country.budget += s0_price*int(message.content.split(" ")[2])
            country.troop += int(message.content.split(" ")[2])
            country.s0 -= int(0.9*int(message.content.split(" ")[2]))
          else:
            user_id = message.author.id    
            await message.channel.send(f"{country_name} - SuperStrength0: {country.s0} - Army: {country.troop} - Budget: {country.budget}")
    if message.content.startswith('/s1'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.s1 += int(0.8*int(message.content.split(" ")[2]))
          country.troop -= int(message.content.split(" ")[2])
          country.budget -= s1_price*int(message.content.split(" ")[2])
          if country.budget < 0 or country.troop < 0:
            await message.channel.send("Violation, not enough budget or not enough troop")
            country.budget += s1_price*int(message.content.split(" ")[2])
            country.troop += int(message.content.split(" ")[2])
            country.s1 -= int(0.8*int(message.content.split(" ")[2]))
          else:
            user_id = message.author.id    
            await message.channel.send(f"{country_name} - SuperStrength1: {country.s1} - Army: {country.troop} - Budget: {country.budget}")
    if message.content.startswith('/s2'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.s2 += int(0.7*int(message.content.split(" ")[2]))
          country.troop -= int(message.content.split(" ")[2])
          country.budget -= s2_price*int(message.content.split(" ")[2])
          if country.budget < 0 or country.troop < 0:
            await message.channel.send("Violation, not enough budget or not enough troop")
            country.budget += s2_price*int(message.content.split(" ")[2])
            country.troop += int(message.content.split(" ")[2])
            country.s2 -= int(0.7*int(message.content.split(" ")[2]))
          else:
            user_id = message.author.id    
            await message.channel.send(f"{country_name} - SuperStrength2: {country.s2} - Army: {country.troop} - Budget: {country.budget}")
    if message.content.startswith('/s3'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.s3 += int(0.6*int(message.content.split(" ")[2]))
          country.troop -= int(message.content.split(" ")[2])
          country.budget -= s3_price*int(message.content.split(" ")[2])
          if country.budget < 0 or country.troop < 0:
            await message.channel.send("Violation, not enough budget or not enough troop")
            country.budget += s3_price*int(message.content.split(" ")[2])
            country.troop += int(message.content.split(" ")[2])
            country.s3 -= int(0.6*int(message.content.split(" ")[2]))
          else:
            user_id = message.author.id    
            await message.channel.send(f"{country_name} - SuperStrength3 : {country.s3} - Army: {country.troop} - Budget: {country.budget}")
    if message.content.startswith('/budget'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.budget += int(message.content.split(" ")[2])
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Budget: {country.budget}")
    if message.content.startswith('/budget2'):
      country_name_send = message.content.split(" ")[1].lower()
      country_name_receive = message.content.split(" ")[2].lower()
      country_send = countries[country_name_send]
      country_receive = countries[country_name_receive]
      country_send.budget -= int(message.content.split(" ")[3])
      country_receive.budget += int(message.content.split(" ")[3])
      await message.channel.send(f"{country_name_send} - Budget: {country_send.budget} - {country_name_receive} - Budget: {country_receive.budget}")
    if message.content.startswith('/aircraft'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.aircraft += int(message.content.split(" ")[2])
          country.budget -= int(message.content.split(" ")[2])*aircraft_price
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Aircraft: {country.aircraft}")
    if message.content.startswith('/ship'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.ship += int(message.content.split(" ")[2])
          country.budget -= int(message.content.split(" ")[2])*ship_price
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Ship: {country.ship}")
    if message.content.startswith('/car'):
      country_name = message.content.split(" ")[1].lower()
      if country_name in countries:
          country = countries[country_name]
          country.car += int(message.content.split(" ")[2])
          country.budget -= int(message.content.split(" ")[2])*car_price
          user_id = message.author.id    
          await message.channel.send(f"{country_name} - Car: {country.car}")
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

@tasks.loop(seconds=60)
async def update_file():
    with open('country_data.txt', 'w') as f:
        for abbrev, country in countries.items():
            f.write(country.country() + '\n')
    print("updated")

  
bot.run("YOUR BOT TOKEN")