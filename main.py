import disnake
from disnake.ext import commands
from  dotenv import  load_dotenv
import logging
from logging.handlers import  RotatingFileHandler
import openai
import os

load_dotenv()
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
if DEBUG:
    print("Режим отладки включен!")

openai.api_key = OPENAI_TOKEN

if not os.path.exists('logs'):
    os.makedirs('logs')

handler = RotatingFileHandler(
    'logs/bot.log', maxBytes=5*1024*1024, backupCount=3, encoding='utf-8'
)
# logging.basicConfig(
#     filename='logs/bot.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
#     encoding='utf-8'
# )


logger = logging.getLogger('bot')
logger.setLevel(logging.INFO)
logger.addHandler(handler)



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
bot.load_extension("cogs.ai_commands")

bot.run(TOKEN)
# print("Загруженные коги:", bot.extensions)
# @bot.event
# async def on_ready():
#     for guild in bot.guilds:
#         for member in guild.members:
#             print(f"{member.name} - {member.status}")
