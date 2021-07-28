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
    print(f'Logged in as {client.user}')

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


if os.path.isfile('./.env'):

    Token = open ('.env' , 'r').read()
    if Token != "":
        if "-" in Token: 
            try:
                client.run(Token)
                print()
                print("The bot has started!")
                print()
            except:
                print("Could not start the bot!🤒")
        else:
            print("ERROR:\
    Invalid token found in the .env file")
    else:
        print("No bot token was found in the .env file! please paste in the correct bot token in the .env file")
else:
    Token = open('.env','w+').read()
    print("TOKEN NOT FOUND PLEASE PASTE THE BOT TOKEN IN THE .env FILE")
    del Token
    # keep_alive()


# client.run(os.getenv('TOKEN'))