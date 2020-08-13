from discord.ext import commands
from pathlib import Path
import subprocess 
import discord


# ======================================================
#
# ADD "token.txt" WITH YOUR BOT TOKEN TO RUN THE BOT!!!
# (it is added to .gitignore so that you won't commit it)
#
# ======================================================

bot = commands.Bot(command_prefix="<")
#bot.remove_command('help')
Discord_Bot_Dir = Path(__file__).parent.absolute()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def hello(ctx):
    if ctx.message.author == bot.user:
        return
    else:
        await ctx.channel.send('Hello!')

@bot.command() 
async def hello2(ctx):
    Bot=subprocess.Popen("../Volume.sh get_volume", stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
    await ctx.channel.send ("Volume is "+str(Bot.stdout))

@bot.command()
async def hello3(ctx):
    if ctx.message.author == bot.user:
        return
    else:
        await ctx.channel.send(ctx.message.content)

@bot.command()
async def hello4(ctx, volume):
    Bot=subprocess.Popen("../Volume.sh change_volume " +volume, shell=True, executable="/bin/bash")
    await ctx.channel.send ("Volume has set to "+str(volume))

@bot.command()
async def hello5(ctx, *question):   
    answer = input(str(ctx.message.author) + " asked this question '" + str(" ".join(question[:]))+"':")
    embed = discord.Embed(
        title="Answer", 
        colour=discord.Colour(0x15c444),
        description=answer)
    await ctx.channel.send(embed=embed)
    
file = open(Discord_Bot_Dir / 'token.txt','rt')
bot.run(str(file.read()))


#"Hello world" + variable
#f"hello World {variable}"