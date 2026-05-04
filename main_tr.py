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
from deep_translator import GoogleTranslator

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

def get_random():
    base_url = "https://uselessfacts.jsph.pl/random.json"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        text_en = data.get("text", "")

        return GoogleTranslator(source='en', target='tr').translate(text_en)
    else:
        return "Rastgele bilgi alınamadı."

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is ready to go')

@bot.command()
async def getrandom(ctx):
    await ctx.send(f"İşte ilginç bir bilgi: {get_random()}")

@bot.command()
async def start(ctx):
    await ctx.reply("Hello, I am ready!")

bot.run(DISCORD_TOKEN) # pyright: ignore[reportArgumentType]