# 
#   ▄▄▄▄▄▄     ▄▄▄▄▄▄▄   ▄▄▄▄▄▄     ▄▄▄▄▄▄     ▄▄▄   
#  █▀██▀▀▀█▄  █▀██▀▀▀   █▀██▀▀██   █▀██▀▀▀█▄  ██▀▀█▄ 
#    ██▄▄▄█▀    ██        ██   ██    ██▄▄▄█▀  ██ ▄█▀ 
#    ██▀▀█▄     ███▀      ██   ██    ██▀▀▀    ██▀▀█▄ 
#  ▄ ██  ██   ▄ ██      ▄ ██   ██  ▄ ██     ▄ ██  ▄█ 
#  ▀██▀  ▀██▀ ▀██▀      ▀██▀███▀   ▀██▀     ▀██████▀ 
# 
# Random Facts Discord Python Bot

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

def get_random():
    base_url = "https://uselessfacts.jsph.pl/random.json"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        return data.get("text", "Could not fetch a fact.")
    else:
        return "Could not fetch a fact."

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready to go!")

@bot.command()
async def getrandom(ctx):
    fact = get_random()
    await ctx.send(f"Here is a random fact: {fact}")

@bot.command()
async def start(ctx):
    await ctx.reply("Hello! I am a simple bot that gives random facts.")

bot.run(DISCORD_TOKEN) # pyright: ignore[reportArgumentType]
