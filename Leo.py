import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

bot.remove_command("help")


@bot.event
async def on_ready():   
    game = discord.Game("and helping")

    await bot.change_presence(status=discord.Status.idle, activity=game)
    
    print('Logged in as')

    print("Leo")
    
    print(bot.user.id)
    
    print('------------------------')


@bot.command()
async def bday(ctx):
    await ctx.send(r"Happy Bday!,Wish you the best day ever. Don't Forget to ENJOY:gift: :gift_heart:",
                   file=discord.File(r'LeoBot\Bday\Images\Bday.gif',
                                 r'LeoBot\Bday\Images\hday.jpg'))
    #   Updated path here. This would make it run remotely too.
    await ctx.message.add_reaction("💝")


@bot.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.dark_magenta()
    )

    embed.set_author(name="Help")
    embed.add_field(name="bday", value="Birthday",inline=False)

    await author.send(author, embed=embed)

@bot.command()
async def clean(ctx):
    textchannel = discord.TextChannel
    channel = textchannel.purge
    messages=[]
    
    async for message in channel.history(channel):
        messages.append(message)

    await discord.delete_messages(messages)
    await ctx.say("Messages Deleted")



bot.run('NTIyODA5MjAzNTM0ODU2MjIy.DvQYUA.lZ5IPIyBQGZBVcqtzaXTXgnuOu0')

