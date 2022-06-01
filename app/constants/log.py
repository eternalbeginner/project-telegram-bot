from typing import Final

LOG_LEVEL_DEBUG: Final    = "debug"
LOG_LEVEL_ERROR: Final    = "error"
LOG_LEVEL_SUCCESS: Final  = "success"
LOG_LEVEL_WARN: Final     = "warn"

LOG_DIR = "app/logs"

LOG_FILE_EXT: Final         = "log"
LOG_FILE_CATEGORIES: Final  = [
  ("debug", [LOG_LEVEL_DEBUG, LOG_LEVEL_SUCCESS]),
  ("error", [LOG_LEVEL_ERROR]),
  ("warn",  [LOG_LEVEL_WARN]),
]

LOG_MESSAGE_FORMATS = {
  "debug" : "{} {:10} {}\n",
  "error" : "{} {:10} {}:\n{}\n",
  "warn"  : "{} {:10} {}\n"
}
