import disnake
from disnake.ext import commands
from  dotenv import  load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
if DEBUG:
    print("Режим отладки включен!")

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} steady!")

bot.load_extension("cogs.basic_commands")
bot.load_extension("cogs.events")

bot.run(TOKEN)
# print("Загруженные коги:", bot.extensions)
# @bot.event
# async def on_ready():
#     for guild in bot.guilds:
#         for member in guild.members:
#             print(f"{member.name} - {member.status}")
