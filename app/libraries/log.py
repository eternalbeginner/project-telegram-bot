from datetime import datetime
from os import path
from app.constants.log import *

class Log:
  def debug(self, message: str) -> None:
    return self.write(
      message,
      LOG_LEVEL_DEBUG
    )


  def error(self, message: str, exception: Exception) -> None:
    return self.write(
      message,
      LOG_LEVEL_ERROR,
      exception
    )


  def success(self, message: str) -> None:
    return self.write(
      message,
      LOG_LEVEL_SUCCESS
    )


  def warn(self, message: str) -> None:
    return self.write(
      message,
      LOG_LEVEL_WARN
    )


  def write(self, message: str, level: str, exception = Exception):
    try:
      log_category = self._get_log_category(level)
      log_path = self._get_log_path(log_category)

      with open(log_path, mode="a") as log_file:
        log_level = level.upper()
        log_message = message.title()
        log_time = datetime.now()

        # if the log level is success, then print the log message
        # to the console
        if level == LOG_LEVEL_SUCCESS:
          print("{:10} {}".format(log_level, log_message))

        log_file.write(LOG_MESSAGE_FORMATS.get(log_category, "{} {:10} {}").format(
          log_time, log_level, log_message, exception
        ))

        log_file.close()
    except BufferError as e:
      print(e)
    except Exception as e:
      print(e)


  def _get_log_category(self, level: str) -> str:
    for category, levels in LOG_FILE_CATEGORIES:
      if level in levels:
        return category

    raise Exception("No category for {}'s level.".format(level))


  def _get_log_path(self, category: str) -> str:
    return path.join(LOG_DIR, "{}.{}".format(
      category,
      LOG_FILE_EXT
    ))


log = Log()
