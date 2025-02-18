from http.client import responses
import disnake
from disnake.ext import commands
import openai


class AICommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx, *, question: str):
        try:
            response = openai.completions.create(
                model="gpt-3.5-turbo",  # Можно использовать и другие модели, например, gpt-4
                prompt=question,
                max_tokens=150
            )
            answer = response['choices'][0]['text'].strip()

            await ctx.send(answer)

        except Exception as e:
            await  ctx.send(f'Error{str(e)}')

def setup(bot):
    bot.add_cog(AICommands(AICommands(bot)))


