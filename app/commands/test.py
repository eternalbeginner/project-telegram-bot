from pyrogram.client import Client
from pyrogram.types.messages_and_media import Message
from typing import List


async def handle(app: Client, message: Message, args: List[str]):
  await message.reply("Hello there!", reply_to_message_id=message.id)
