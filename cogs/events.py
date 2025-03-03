import disnake
from  disnake.ext import commands
import logging

logger = logging.getLogger('bot.events')

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        logger.info(f"Событие on_member_update сработало для {after.name}")  # Проверка

        if before.status != after.status:
            logger.info(f"Статус изменился: {before.status} → {after.status}")  # Проверка статуса

        guild = after.guild
        if guild is None:
            logger.warning('cant find channel for message')
            return

        channel = disnake.utils.get(guild.text_channels, name="общее")

        if channel is None:
            logger.warning('wrong name ch')
            return

        if before.status != after.status and after.status == disnake.Status.online:
            logger.info(f"{after.name} зашел, отправляю сообщение в {channel.name}")
            await channel.send(f'{after.name} Зашел, поприветствуем!')


def setup(bot):
    bot.add_cog(Events(bot))

        # print(f"{after.name} изменил статус: {before.status} → {after.status}")  # Отладка статуса
        #
        # if before.status != after.status and after.status == disnake.Status.online:
        #     channel = self.bot.get_channel("1337598195794186283")  # Проверяем канал
        #     if channel is None:
        #         print("Ошибка: Канал не найден! Проверьте ID канала.")
        #     else:

    # @commands.Cog.listener()
    # async  def on_message(self,message):
    #     if message.author == self.bot.user:
    #         return
    #     print(f'Новое сообщение от {message.author}: {message.content}')
    #     await self.bot.process_commands(message)
