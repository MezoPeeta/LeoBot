import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='and helping'))
    print('LEO IS HEREEEEE')

@client.event
async def on_message(message):
    if message.content.startswith('$messages'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit = 100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

        
    elif message.content.startswith('$bday'):
        await client.send_message(message.channel, "HAPPYBIRTHDAAAY!, Wish you the best day ever. Don't Forget to ENJOOOOOOOOOOOOOY :blush: :gift: :gift_heart:")
        await client.send_file(message.channel, 'E:\WorkSpace\Python\Leo\LeoBot\Gif\Bday.gif')
        await client.add_reaction("bday", "💝")

    
client.run('NTIyODA5MjAzNTM0ODU2MjIy.DvQYUA.lZ5IPIyBQGZBVcqtzaXTXgnuOu0')
