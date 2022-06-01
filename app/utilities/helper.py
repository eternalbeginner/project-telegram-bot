from pyrogram.types.messages_and_media import Message
from typing import List, Tuple
from app.libraries import env, log


def get_command_data(message: Message) -> Tuple[str, List[str]]:
  message_sender    = message.from_user
  message_segments  = message.text.split(" ", 1)

  log.debug("New message from: {}".format(
    message_sender.username or message_sender.first_name
  ))

  if message_segments[0][0] != env.get("APP_BOT_PREFIX", "/"):
    return None

  command   = message_segments.pop(0)
  arguments = message_segments[0].split(" ") if len(message_segments) != 0 else []

  return (command, arguments)
