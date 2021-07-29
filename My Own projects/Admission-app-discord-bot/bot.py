import os
try:
    import time
    import discord
    from keep_alive import keep_alive
    from discord.ext import commands
    from discord_slash import SlashCommand, SlashContext
    from discord_slash.utils.manage_commands import create_choice,create_option

except ModuleNotFoundError:
    os.system('python -m pip install -r requirements.txt')

def Welcome_Message(usr_id,bot_id):
    message_welcome = (f'Hello <@{usr_id}>!\n'
                       f'Thank you for using <@{bot_id}> made by <@765739254164357121>\n'
                       f'You will will have to answer the following questions in order to get enroled.\n'
                       f'So please answer the following questions promtly.')
    
    return message_welcome

client = commands.Bot(command_prefix='ah!')
slash = SlashCommand(client,sync_commands=True)


@slash.slash(name="Create",
             description="Will create an admission for you",
             
             options=[
               create_option(
    
                 name="email",
                 description="Please enter your email. We won`t spam you.",
                 option_type=3,
                 required=True,
                 )
             ])

async def test(ctx,email:str):

    global user_name
    user_name = (str(ctx.author)).replace(f'#{str(ctx.author.id)}' , '')
    user_id = (str(ctx.author.id))
    
    bot_id = (int(client.user.id))

    await ctx.send(content=f"<@{user_id}> check your dms for the application form")
    
    await ctx.author.send(Welcome_Message(usr_id=user_id,bot_id=bot_id))

@client.event 
async def on_ready():
    print(f'Logged in as {client.user}')
    print()
    print('The bot is now online!')

async def on_message(message):
    if message.author == client.user:
        return


    msg = message.content

    if msg:
        print(f'{message.author}: {msg} ({message.channel})')

# keep_alive()
if os.path.isfile('./.env'):
    try:

        token = os.getenv("TOKEN")
    except:
        with open('.env','w+') as environment_var:
            environment_var.write("TOKEN=")
        print("Error: Bot token not found!\n\
   please paste the bot token in the .env file next to 'TOKEN='")

        print("\n"*2)
        input('Press enter to quit')
        exit()

    if token != '':
        if '-' in token:
            try:
                client.run(token)
            except:
                print("Invalid Token please regenerete the token and try again")
                print("*"*2)
                input("Press enter to quit")
                exit()
        else:
            print("Invalid Token please regenerete the token and try again")
            print("*"*2)
            input("Press enter to quit")
            exit()
    else:
        print("Error: Bot token not found!\n\
       please paste the bot token in the .env file next to 'TOKEN='")
        print("\n"*2)
        input('Press enter to quit')

else:
    with open('.env','w+') as environment_var:
        environment_var.write("TOKEN=")
    print("Error: Bot token not found!\n\
       please paste the bot token in the .env file next to 'TOKEN='")
    print("\n"*2)
    input('Press enter to quit')
    exit()
