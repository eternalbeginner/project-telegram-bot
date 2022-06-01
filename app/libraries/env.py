from dotenv import dotenv_values
from typing import OrderedDict
from app.constants.env import *


class Env:
  repository: OrderedDict

  def __init__(self):
    self.repository = dotenv_values(ENV_FILE_NAME)


  def get(self, key: str, default: str="") -> str:
    return self.repository.get(
      key,
      default
    )


  def set(self, key: str, value: str) -> str:
    return self.repository.update({
      [key]: value
    })


env = Env()
