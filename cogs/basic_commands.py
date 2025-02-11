import disnake
from  disnake.ext import commands

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Привет, {ctx.author.mention} , я бот. Напиши !help для списка комманд.')

    @commands.command()
    async def server(self, ctx):
        await ctx.send(f'Сервер {ctx.guild}, канал {ctx.channel}')


def setup(bot):
    bot.add_cog(BasicCommands(bot))










# def setup(bot):
#     @bot.command()
#     async def hello(ctx):
#         await ctx.send(f'Привет, {ctx.author.mention} , я бот. Напиши !help для списка комманд.')
#         await ctx.send(f'Ты {ctx.author}, name {ctx.author.name}, другое {ctx.author.mention}, '
#                        f', время сообщения {ctx.message.created_at}')

#     @bot.command()
#     async def server(ctx):
#         await ctx.send(f'Сервер {ctx.guild}, канал {ctx.channel}')
#
