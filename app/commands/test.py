from pyrogram.client import Client
from pyrogram.enums.chat_type import ChatType
from pyrogram.types.messages_and_media import Message
from typing import List
from app.constants.role import *

__restriction__ = [ROLE_ADMIN, ROLE_STAFF]
__visibility__  = [ChatType.SUPERGROUP, ChatType.GROUP, ChatType.PRIVATE]


async def handle(app: Client, message: Message, args: List[str]):
  await message.reply("Hello there!", reply_to_message_id=message.id)
