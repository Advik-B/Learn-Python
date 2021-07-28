import time
import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

line_break = "> || ||"

def get_quote():
    while True:
        try:

            response = requests.get("https://zenquotes.io/api/random")
        except requests.ConnectionError:
            return "Sorry but we are unable to load the quotes"

        if response != '[{"q":"Too many requests. Obtain an auth key for unlimited access.","a":"zenquotes.io","h":"Too many requests. Obtain an auth key for unlimited access @ zenquotes.io"}]':
            json_data = json.loads(response.text)
            quote = json_data[0]['q'] + " -" + json_data[0]['a']
            return(quote)
        else:
            continue #looping until you get a proper responce

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
        outquote = True
        if msg != '$quote':
            try:

                number = int(msg.split('$quote ',1)[1])
                for i in range(number-1):
                    quote = get_quote()
                    if quote != 'Sorry but we are unable to load the quotes':

                        await message.channel.send(f'{quote} \n{line_break}')
                        time.sleep(4)
                    else:
                        await message.channel.send('Sorry but my quotes are not able to load please try again in 30 seconds')
                        break
                    
                del i

            except:
                error_cause = str(msg.split('$quote ',1)[1])

                await message.channel.send(f'**INVALID COMMAND:**\n\
    ***`$quote {error_cause}`*** is not a valid command since ***`{error_cause}`*** is not a number')
                outquote = False
        
        if outquote != False:
            await message.channel.send(f'{quote}\n')
        else:
            outquote = True


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