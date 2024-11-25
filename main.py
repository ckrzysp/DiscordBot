# Import Discord Package or anything from the libraries
import discord
from discord.ext import commands
from openai import OpenAI
from key import *

# Client (Bot)

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = ",", intents=discord.Intents.all())

# Functionality

# bot status / ON_READY
@client.event
async def on_ready():
    float = client.latency * 1000
    print("Bot is online!")
    print(float)
    await client.change_presence(
        status = discord.Status.idle, 
        activity = discord.Game
        ("prefix is ',' do ,cmds"))

# Commands
@client.command(name = 'cmds')
async def embed(message):

    embedB = discord.Embed(title = "KrzysioBot commands", description = "test", color = 0x0efa9c)
    
    embedB.add_field(name = 'Category', value = 'Description', inline = False)
    
    embedB.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/506958296343904256/779117487391899668/Sharp.png')
    embedB.set_footer(text = "From Krzysio#9449")

    await message.send(embed = embedB)


@client.command(name = 'add')
async def func(ctx, arg1, arg2):
    try:
        result = int(arg1) + int(arg2)
        await ctx.send(result);
    except:
        await ctx.send("Not a number")


AIclient = OpenAI(api_key='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')

@client.command(name = 'gpt')
async def func(message, *args): 
    words = ' '.join(args)
    
    completion = AIclient.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are smart AI"},
            {
                "role": "user",
                "content": words
            }
    ]
    )

    embedB = discord.Embed(description = completion.choices[0].message.content, color = 0x0efa9c)
    await message.send(embed = embedB)

@client.command(name = 'join')
async def func(ctx, arg1, arg2):
    try:
        result = int(arg1) + int(arg2)
        await ctx.send(result);
    except:
        await ctx.send("Not a number")
# API integration and commands
    

# // RUN //
token = bottoken
client.run(token)