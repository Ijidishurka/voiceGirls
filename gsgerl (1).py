# модуль голсовые сообщения девушек
# подпишись на тг канал @modwini
from .. import loader


@loader.tds
class voiceGirls(loader.Module):
    """Голосовые сообщения девушек by @modwini"""

    strings = {"name": "voiceGirls"}

    async def voice1cmd(self, message):
        """Приветик"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/195",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice2cmd(self, message):
        """Как дела?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/198",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice3cmd(self, message):
        """Да"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/197",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice4cmd(self, message):
        """Нет"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/196",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice5(self, message):
        """очень жаль"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/199",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice6cmd(self, message):
        """я тебе не доверяю"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/200",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice7cmd(self, message):
        """подожди"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/201",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice8cmd(self, message):
        """спокойной ночи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/202",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice9cmd(self, message):
        """ясно"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/203",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice10cmd(self, message):
        """я обиделась"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/204",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice11cmd(self, message):
        """ты мне нравишся"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/205",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice12cmd(self, message):
        """мур"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/206",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice14cmd(self, message):
        """ну пожалуйста"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/207",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice15cmd(self, message):
        """спасибо"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/208",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice16cmd(self, message):
        """Ну ты где?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/209",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice17cmd(self, message):
        """Договорились"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/210",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice18cmd(self, message):
        """Доброе утро"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/211",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice19cmd(self, message):
        """К сожалению не могу"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/212",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice20cmd(self, message):
        """Нипоняла"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/213",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice21cmd(self, message):
        """Расскажи мне интересно"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/214",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice22cmd(self, message):
        """Чмоки чмоки"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/215",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice23cmd(self, message):
        """Спокойной ночи тебе"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/216",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice24cmd(self, message):
        """А ты меня любишь?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/217",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice25cmd(self, message):
        """Ну котик"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/218",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice26cmd(self, message):
        """Котик"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/219",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice27cmd(self, message):
        """Ну блин"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/220",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def voice28cmd(self, message):
        """Скоро буду"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/221",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return