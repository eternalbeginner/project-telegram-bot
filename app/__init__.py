from pyrogram.client import Client
from app.libraries import env, log

class Bot:
  bot: Client

  def __init__(self):
    log.debug("Initializing application")

    api_id        = env.get("APP_API_ID")
    api_hash      = env.get("APP_API_HASH")
    bot_token     = env.get("APP_BOT_TOKEN")
    session_name  = env.get("APP_SESSION_NAME")
    plugins       = { "root": "app/handlers" }

    self.bot = Client(
      session_name,
      api_id,
      api_hash,
      bot_token=bot_token,
      plugins=plugins
    )

    log.success("Application initialized")


  def launch(self) -> None:
    try:
      with self.bot:
        if self.bot.is_connected is None:
          self._reconnect()

        log.success("Application started")
        self.bot.loop.run_forever()
    except KeyboardInterrupt as e:
      log.warn("Keyboard interruption")
      log.success("Application stopped")
      exit(0)
    except Exception as e:
      log.error("Exception occured", e)
      exit(1)


  def _reconnect(self):
    log.warn("Application isn't connected")
    log.debug("Reconnecting application")

    self.bot.connect()

    log.success("Application reconnected")
