from http.client import responses
import disnake
from disnake.ext import commands
import openai
from main import OPENAI_TOKEN

openai.api_key = OPENAI_TOKEN

class AICommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx, *, question: str):
        try:
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=question,
                max_tokens=150
            )
            answer = response.choices[0].text.strip()

            await ctx.send(answer)

        except Exception as e:
            await  ctx.send(f'Error{str(e)}')

def setup(bot):
    bot.add_cog(AICommands(AICommands(bot)))


