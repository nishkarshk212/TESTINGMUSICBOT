#!/usr/bin/env python3
from config import Config
config = Config()
print("API_ID:", config.API_ID)
print("API_HASH:", config.API_HASH)
print("BOT_TOKEN:", config.BOT_TOKEN)
print("MONGO_URL:", config.MONGO_URL)
print("LOGGER_ID:", config.LOGGER_ID)
print("OWNER_ID:", config.OWNER_ID)
print("SESSION1:", config.SESSION1)
try:
    config.check()
    print("Config check passed!")
except SystemExit as e:
    print("Config check failed:", e)
