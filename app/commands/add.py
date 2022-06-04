from pyrogram.client import Client
from pyrogram.enums.chat_type import ChatType
from pyrogram.types.messages_and_media import Message
from typing import List
from app.constants.role import *
from app.libraries import db, log

__restriction__ = [ROLE_ADMIN]
__visibility__  = [ChatType.SUPERGROUP, ChatType.GROUP, ChatType.PRIVATE]


async def handle(app: Client, message: Message, args: List[str]):
  db_roles  = db.use("roles")
  msg_id    = message.id

  # check for the arguments length, if below 1 or equal to 0
  # then log it and send an message
  if len(args) < 1:
    log.warn("Invalid arguments length for command add")

    await message.reply(
      "Argumen untuk command ini tidak sesuai",
      reply_to_message_id=msg_id
    )

    return

  # ensure the role is a valid role
  if args[0] not in AVAILABLE_ROLES:
    log.warn("Invalid role type added: {}".format(args[0]))

    await message.reply(
      "Tidak ada role yang bernama {}".format(args[0]),
      reply_to_message_id=msg_id
    )
    
    return

  person = None

  # ensure if the user mention or reply to any message
  # before adding the mentioned or replied user
  # role
  if len(args) == 1 and message.reply_to_message is None:
    await message.reply(
      "Mention atau reply user yang ingin ditambahkan",
      reply_to_message_id=msg_id
    )

    raise Exception("Adding {} but with no person identifier".format(args[0]))
  elif len(args) == 1 and message.reply_to_message is not None:
    # get the user's data from the replied message sender
    person = message.reply_to_message.from_user
  elif len(args) == 2:
    # get the user's data from the mentioned user
    person = await app.get_users(args[1])

  log.debug("Data for user: {}'s collected".format(person.username or person.first_name))
  log.debug("Updating database: roles")
  db_roles.update(args[0], person.id)

  await message.reply(
    "Berhasil menambahkan {} sebagai {}".format(
      person.username or person.first_name,
      args[0]
    ),
    reply_to_message_id=msg_id
  )

  log.success("{} is added as a {}".format(
    person.username or person.first_name,
    args[0]
  ))
