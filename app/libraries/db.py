from json import dump, load
from os import path
from typing import Any, Dict
from app.constants.db import *

class Db:
  current: Dict[str, Any]
  current_name: str


  def create(self, key: str, value: Any) -> None:
    if not self._is_db_used():
      raise Exception("Currently no DB is used")

    self.current.update({ [key]: value })
    self._set_db_data(self.current)


  def get(self, key: str="*", default: Any=None):
    if not self._is_db_used():
      raise Exception("Currently no DB is used")

    # if the key is * then that means we want to get all
    # data of the currently db used
    if key == "*":
      return self.current

    return self.current.get(key, default)

  
  def update(self, key: str, value: Any) -> None:
    if not self._is_db_used():
      raise Exception("Currently no DB is used")

    # if there are no key matching, then log it to the log file
    # and return immediately
    if key not in self.current.keys():
      raise Exception("No key named: {} in database: {}".format(key, self.current_name))

    self.current.update({ [key]: value })
    self._set_db_data(self.current)


  def use(self, name: str):
    try:
      db_path = self._get_db_location(name)

      if not path.isfile(db_path):
        raise Exception("Can't find database with name: {}".format(
          name
        ))

      with open(db_path, mode="r") as db_file:
        self.current      = load(db_file)
        self.current_name = name

        return self
    except BufferError:
      raise Exception("Failed when reading database: {}".format(name))


  def _get_db_location(self, name: str) -> str:
    return path.join(DB_DIR, "{}-{}.{}".format(
      DB_FILE_PREFIX,
      name,
      DB_FILE_EXTENSION
    ))


  def _is_db_used(self):
    return self.current is not None


  def _set_db_data(self, data: Any) -> None:
    try:
      if not self._is_db_used():
        raise Exception("Currently no DB selected")

      db_path = self._get_db_location(self.current_name)

      with open(db_path, mode="w", encoding="utf-8") as db_file:
        dump(data, db_file, ensure_ascii=False, indent=2)
    except BufferError:
      raise Exception("Failed when reading database: {}".format(self.current_name))


db = Db()