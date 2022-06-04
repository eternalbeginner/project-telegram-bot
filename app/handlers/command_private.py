from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types.messages_and_media import Message
from app.constants.command import *
from app.libraries import db, env, log
from app.utilities import helper


@Client.on_message(filters.private & filters.text)
async def handler(app: Client, message: Message):
  db_roles = db.use("roles").get()

  msg_id = message.id
  msg_sender = message.from_user

  try:
    log.debug("Executing handler for private sended message")

    cmd, args = helper.get_command_data(message)
    cmd_name  = cmd.replace(env.get("APP_BOT_PREFIX"), "")

    # if we can't find the command's handler file, the we
    # will log it and send a confirmation message that
    # says the command is invalid
    if not helper.is_command_exists(cmd_name):
      log.warn("Can't find command's handler for: {}".format(cmd_name))

      await message.reply(
        "Itu bukan command yang valid.",
        reply_to_message_id=msg_id
      )

      return

    cmd_module = helper.import_command_module(cmd_name)

    # check for the command visibility, either the command is available
    # for all chat type or only for a spesific chat type
    if message.chat.type not in cmd_module.__visibility__:
      log.warn("Command: {} isn't available on private chat".format(cmd_name))

      await message.reply(
        "Command ini tidak tersedia untuk private chat",
        reply_to_message_id=msg_id
      )

      return

    # check if the command handler hold for some roles restriction, then check
    # if the sender of the message is allowed to use the command
    if not helper.is_sender_authorized(msg_sender.id, cmd_module.__restriction__, db_roles):
      log.warn("{} try to access authorized command".format(
        msg_sender.username or msg_sender.first_name
      ))

      await message.reply(
        "Kamu tidak punya akses untuk command ini",
        reply_to_message_id=msg_id
      )

      return

    # if the command's handler isn't have the handler property (function),
    # then we will raising exception to log the error to the log file
    if not hasattr(cmd_module, "handle"):
      raise Exception("Handler for: {} isn't have handler property".format(cmd_name))

    log.debug("Executing handler for command: {}".format(cmd_name))

    await cmd_module.handle(
      app,
      message,
      args
    )

    log.success("Handler for command: {}'s executed".format(cmd_name))
  except Exception as e:
    log.error("Handler exception occured", e)

    # send information about exception's captured to the admins
    for admin_id in db_roles.get("admin"):
      await app.send_message(admin_id, "Exception occured:\n{}".format(e))
