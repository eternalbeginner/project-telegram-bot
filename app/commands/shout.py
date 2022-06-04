from pyrogram.client import Client
from pyrogram.enums.chat_type import ChatType
from pyrogram.types.messages_and_media import Message
from pyrogram.types.user_and_chats import User
from typing import List
from app.constants.role import *

__restriction__ = [ROLE_ADMIN, ROLE_STAFF]
__visibility__  = [ChatType.GROUP, ChatType.SUPERGROUP]


async def handle(app: Client, message: Message, args: List[str]):
  msg_id        = message.id
  msg_chat_id   = message.chat.id
  msg_template  = "Hey kalian!\n\n{}\n\nMunculah!"
  members       = []

  async for member in app.get_chat_members(msg_chat_id):
    if member is not None:
      user: User      = member.user
      mention_string  = "@{}".format(
        user.username
      ) if user.username else user.mention()

      members.append(mention_string)

  msg_template = msg_template.format("\n".join(members))

  await message.reply(
    msg_template,
    reply_to_message_id=msg_id
  )
