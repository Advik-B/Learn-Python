from time import time
import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
import time

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$quote'):
    quote = get_quote()
    number = int(msg.split('$quote ',1)[1])
    for i in range(number):
        await message.channel.send(quote)
        time.sleep(1800)

keep_alive()
client.run(os.getenv('TOKEN'))