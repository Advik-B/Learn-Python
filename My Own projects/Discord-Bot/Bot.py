import discord
import random
import time



command_activation = '$'

invite = 'https://discord.gg/aSrpqSbjfz'

bot_token = 'YOUR BOT TOKEN HERE'

bot_name = 'Admission app'

owner = '<@765739254164357121>'

owner_admin = '<@!765739254164357121>'

client = discord.Client()

hi_messages  = [
    'Hi!' ,
    'Hi',
    'hi',
    'hI',
    'Weclome',
    'weclome',
    'Heyoo!' ,
    'Wassup' ,
    'wassup',
    'Hey' ,
    'hey',
    'Bye.:rofl:' ,
    'sup' ,
    'Sup',
    'Yo' ,
    'yo' ,
    ]


server = 'G̵A̷M̸M̷E̶R̸Z̸'

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):

    """
    
    These are my custom commands
    
    """

    if message.content == f'{command_activation}spam-shit':
        await message.channel.send('THIS IS FUCKING ANNOYING LOL \n'*20)
    
    if message.content == f'{command_activation}spam':
        await message.channel.send(f'Type {command_activation}spam-shit to do that')
    
    if message.content == f'{command_activation}invite':
        await message.channel.send(f'🅹🅾🅸🅽 🅾🆄🆁 🅳🅸🆂🅲🅾🆁🅳 🅰🆃\n'
                                   f'{"🠗"*(len(invite)-2)}\n'
                                   f'{invite}')
    if message.content == f"{command_activation}owner":
        await message.channel.send(f'My owner is {owner}')

    if message.content == f"{command_activation}help":
        await message.channel.send(
        f"The commands are:\n"
        f"  {command_activation}invite\n"
        f"  {command_activation}spam-shit\n"
        f"  {command_activation}owner\n")

    if message.content == f"{command_activation}play":
        for i in range(5):
            await message.channel.se('/play input:BTS ')
            time.sleep(2.05)

    if message.content:
        if message.author != client.user:
            
            print(f'{message.author}: {message.content} ({message.channel})')
            print()
            if message.content in hi_messages:
                await message.channel.send(hi_messages[random.randint(0,(len(hi_messages)) - 1)])
        if message.content == owner or message.content == owner_admin:
            await message.channel.send(f'Hey {owner} is my dad')
            
client.run(bot_token)