# Import Discord Package or anything from the libraries
import discord
from discord.ext import commands
from openai import OpenAI
import yt_dlp as youtube_dl
from key import *
import os

# Client (Bot)

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = ",", intents=discord.Intents.all())

# Functionality

# Bot Status / ON_READY
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

    embedB = discord.Embed(title = "KrzysioBot commands", color = 0x0efa9c)
    
    embedB.add_field(name = 'Bot Commands', value = ',gpt [] - Intergrated ChatGPT\n,add [#] [#] - Give two numbers to add\n,j - Join voicechat\n,d - Disconnect from voicechat', inline = False)
    
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

# API integration and command

AIclient = OpenAI(api_key='YOUR API HERE')

@client.command(name = 'gpt')
async def func(message, *args): 
    words = ' '.join(args)
    completion = AIclient.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", 
             "content": "Find me youtube video links. You will be asked ONLY provide a youtube link based on the information given. Make sure the content is accessible."},
            {
                "role": "user",
                "content": words
            }
    ]
    )
    embedB = discord.Embed(description = completion.choices[0].message.content, color = 0x0efa9c)
    await message.send(embed = embedB)

@client.command(name = 'j', pass_context = True)
async def join(ctx):
    try:
        voiceid = ctx.author.voice.channel
        await voiceid.connect()
        await ctx.send("Connected.")
    except:
        await ctx.send("User is not in a voice channel.")

@client.command(name = 'd', pass_context = True)
async def disc(ctx):
    # VoiceChannel, VoiceState issue DOES NOT HAVE DISCONNECT
    try:
        await client.voice_clients[0].disconnect()
        await ctx.send("Disconnected.")
    except:
        await ctx.send("No bot in voice channel.")
    
@client.command(name = 'mt', pass_context = True)
async def func(ctx):
    try:
        await client.voice_clients[0].move_to(ctx.author.voice.channel)
    except:
        await ctx.send("No user connected.")

## Global

YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'webm',
        'preferredquality': '192',
    }],
    'noplaylist': True,
}

FFMPEG_OPTIONS = {
    'executable': "C:/ffmpeg/bin/ffmpeg.exe",
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

@client.command(name = 'play', pass_context = True)
async def func(ctx, url: str):
    # Plays Men At Work - Down Under
    # https://www.youtube.com/watch?v=EeeBH294v6I&list=RDEeeBH294v6I&start_radio=1

    info = ytdl.extract_info(url, download=False)
    url2 = info['url']
    print(url2)
    client.voice_clients[0].play(discord.FFmpegPCMAudio(source=url2, **FFMPEG_OPTIONS), 
                                 after=lambda e: print("Finished playing"))
    
@client.command(name = 'pt', pass_context = True)
async def func(ctx):
    # Plays Men At Work - Down Under
    # https://www.youtube.com/watch?v=EeeBH294v6I&list=RDEeeBH294v6I&start_radio=1

    client.voice_clients[0].play(discord.FFmpegPCMAudio(source='BG.mp3', 
                                                        executable='C:/ffmpeg/bin/ffmpeg.exe'))

@client.command(name = 'p', pass_context = True)
async def func(ctx):
    # Pause current track
    client.voice_clients[0].pause();

@client.command(name = 'r', pass_context = True)
async def func(ctx):
    # Resume current track
    client.voice_clients[0].resume();

    

# // RUN //
token = bottoken
client.run(token)
