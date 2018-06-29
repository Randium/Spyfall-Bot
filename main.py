from check import is_command, import_data, save
import discord
import asyncio
import config
import check
import game

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    main_guild = client.get_channel(config.welcome_channel).guild
    messenger = message.author
    temp_msg = []
    
    # Code here
    if game.game_going_on() == False:
        # Check if the user hasn't signed up yet
        if game.is_playing(messenger.id,config.signees_file):
            if is_command(message,['start']):
                await message.channel.send("We're gonna start the game in 15 seconds! Get ready!")
                await asyncio.sleep(15.0)
                await message.channel.send("Starting game! *cough cough* TODO")
        else:
            if is_command(message,['join','signup']):
                if check.modes(message) == False:
                    save(import_data().append())
                
    
    await asyncio.sleep(5)
    for msg in temp_msg:
        await msg.delete()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.get_channel(config.welcome_channel).send('Beep boop! I just went online!')

client.run(config.TOKEN)
