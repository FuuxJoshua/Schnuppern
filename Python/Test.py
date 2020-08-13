from discord.ext import commands
from pathlib import Path
import subprocess 
import discord
import requests
import psutil
from itertools import chain
from colour import Color
import random

JoshuaDiscordID=691349925165793311

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

@bot.command()
async def hello6(ctx, *command): 
    if ctx.message.author.id==JoshuaDiscordID :
        Bot=subprocess.check_output (str(" ".join(command[:])), stderr=subprocess.STDOUT, shell=True, executable="/bin/bash").decode("ascii")
        await ctx.channel.send (str(Bot))

@bot.command()
async def hello7(ctx, Username):
    response = requests.get(f"https://api.github.com/users/{Username}")
    json=response.json()
    print(json["avatar_url"])
    embed = discord.Embed(
        title="Github Profile", 
        colour=discord.Colour(0x15c444),
        description="Show user profile")
    embed.set_image(url=json["avatar_url"])
    embed.add_field(name="Name", value=json["name"])
    embed.add_field(name="Username", value=json["login"])
    embed.add_field(name="Company", value=json["company"])
    embed.add_field(name="Followers", value=json["followers"])
    embed.add_field(name="Following", value=json["following"])
    embed.add_field(name="ID", value=json["id"])
    embed.add_field(name="HTML URL", value=json["html_url"])
    await ctx.channel.send(embed=embed)


@bot.command()
async def hello8(ctx, delete):
    delete=int(delete)
    if delete <100: 
        await ctx.channel.purge(limit=delete+1)
    else:
        await ctx.channel.send("A maximum of 100 messeges can be deleted per command")


@bot.command()
async def hello9(ctx):
    Ram_usage=psutil.virtual_memory().percent
    Cpu_usage=psutil.cpu_percent()
    colourlist=list(Color("green").range_to(Color("red"), 100))
    print(int(Ram_usage))
    colour=int("0x" + str(colourlist[int(Cpu_usage)])[1:], 16)
    embed = discord.Embed(
        colour=discord.Colour(colour),
        description="RAM usage is " + str(Ram_usage) + "%")
    embed.add_field(name="CPU Usage", value=str(Cpu_usage))
    await ctx.channel.send(embed=embed)


@bot.command()
async def bye(ctx):
    await ctx.channel.send(random.randrange(1, 200))

@bot.command()
async def bye2(ctx):
    sentencelist = ['Hello World', 'Bye World']
    #await ctx.channel.send(random)
    print("random item from list is: ", random.choice(sentencelist))


file = open(Discord_Bot_Dir / 'token.txt','rt')
bot.run(str(file.read()))


#"Hello world" + variable
#f"hello World {variable}"