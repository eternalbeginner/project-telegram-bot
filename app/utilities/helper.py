from importlib import import_module
from json import load
from os import path
from pyrogram.types.messages_and_media import Message
from typing import List, Tuple
from app.constants.command import *
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


def import_command_module(name: str):
  return import_module("{}.{}".format(
    COMMAND_PACKAGE_NAME,
    name
  ))


def import_json_data(name: str):
  db_name = "data-{}.json".format(name.lower())
  db_path = path.join("app/databases", db_name)

  try:
    with open(db_path, mode="r") as db_file:
      return load(db_file)
  except BufferError as e:
    log.error("Buffer exception occured", e)
    pass
  except Exception as e:
    log.error("Exception occured", e)
    pass

  return {}


def is_command_exists(name: str) -> bool:
  return path.isfile(path.join(
    COMMAND_DIR,
    "{}.py".format(name)
  ))


def is_sender_authorized(id: int, restriction: List[str], roles: List[int]) -> bool:
  if len(restriction) == 0:
    # return true if there isn't roles restriction is set
    return True
  else:
    for role_name in restriction:
      if id in roles[role_name]:
        return True

  return False
