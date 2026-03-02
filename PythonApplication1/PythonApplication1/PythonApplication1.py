import discord
from discord import emoji
import dotenv
import os
dotenv.load_dotenv()
token = os.getenv("TOKEN")
UID = 703989551613345793
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
client = discord.Client(intents=intents)
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author.id == UID:
        try:
            await message.add_reaction("🥚")
        except discord.Forbidden:
            print("invalid permission")
        except discord.HTTPException as e:
            print(e)
        except Exception as e:
            print(e)
    print(message.author)
client.run(token)
