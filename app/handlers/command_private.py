from importlib import import_module
from os import path
from pyrogram import client, filters
from pyrogram.types.messages_and_media import Message
from app.constants.command import *
from app.libraries import env, log
from app.utilities import helper


@client.Client.on_message(filters.private & filters.text)
async def handler(app: client.Client, message: Message):
  try:
    cmd, args = helper.get_command_data(message)
    cmd_name = cmd.replace(env.get("APP_BOT_PREFIX"), "")

    # if we can't find the command's handler file, the we
    # will log it and send a confirmation message that
    # says the command is invalid
    if not path.isfile(path.join(COMMAND_DIR, "{}.py".format(cmd_name))):
      log.warn("Can't find command's handler for: {}".format(cmd_name))
      await message.reply("Itu bukan command yang valid.", reply_to_message_id=message.id)
      return

    cmd_handler = import_module("{}.{}".format(COMMAND_PACKAGE_NAME, cmd_name))

    # if the command's handler isn't have the handler property (function),
    # then we will raising exception to log the error to the log file
    if not hasattr(cmd_handler, "handle"):
      raise Exception("Handler for: {} isn't have handler property".format(cmd_name))

    await cmd_handler.handle(app, message, args)
  except Exception as e:
    log.error("Exception occured", e)
