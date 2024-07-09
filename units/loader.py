import json
from types import SimpleNamespace

class Loader:
  def __init__(self, file):
    with open(file, "r") as f:
      self.data = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
  
  def __getattr__(self, name):
    return getattr(self.data, name)

txt = Loader("bot_texts.json")
config = Loader("config.json")