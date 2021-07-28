import time
import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

def get_quote():

    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event 
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event #epic
async def on_message(message):
    if message.author == client.user:
        return


    msg = message.content

    if msg:
        print(f'{message.author}: {msg} ({message.channel})')


    if msg.startswith('$quote'):
        quote = get_quote()
        if msg != '$quote':
            try:

                number = int(msg.split('$quote ',1)[1])
                for i in range(number-1):
                    await message.channel.send(f'{quote} \n{"-"*(len(quote))}')
                    quote = get_quote()
                    if i == 5:
                        time.sleep(5.555)
                del i

            except:
                error_cause = str(msg.split('$quote ',1)[1])

                await message.channel.send(f'**INVALID COMMAND:**\n\
    ***`$quote {error_cause}`*** is not a valid command since ***`{error_cause}`*** is not a number')
                outquote = False
        
        if outquote != False:
            await message.channel.send(f'{quote}\n{"-"*(len(quote))}')
        else:
            pass
try:
    if os.path.isfile('./.env'):

        Token = open ('.env' , 'r').read()
        try:
            client.run(Token)
        except:
            print("INVALID TOKEN")
    else:
        Token = open('.env','w+').read()
    # keep_alive()



except FileNotFoundError:
    print("FATAL ERROR: .env file is not found please create a .env file and paste the bot token inside it")
# client.run(os.getenv('TOKEN'))