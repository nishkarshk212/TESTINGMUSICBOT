print("Hello from simple test!")
import sys
print("Python path:", sys.path)
try:
    from config import Config
    print("Imported Config")
    config = Config()
    print("Config created")
    print("API_ID:", config.API_ID)
    print("API_HASH:", config.API_HASH)
    print("BOT_TOKEN:", config.BOT_TOKEN)
    print("MONGO_URL:", config.MONGO_URL)
    print("LOGGER_ID:", config.LOGGER_ID)
    print("OWNER_ID:", config.OWNER_ID)
    print("SESSION1:", config.SESSION1)
    print("YT_API_KEY:", config.YT_API_KEY)
    print("YTPROXY_URL:", config.YTPROXY_URL)
    try:
        config.check()
        print("Config check passed!")
    except SystemExit as e:
        print("Config check failed:", e)
except Exception as e:
    import traceback
    print("Error:", e)
    traceback.print_exc()
