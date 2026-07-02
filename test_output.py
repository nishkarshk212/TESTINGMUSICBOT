with open('test_output.txt', 'w') as f:
    f.write("Hello from test_output!\n")
    import sys
    f.write(f"Python executable: {sys.executable}\n")
    f.write(f"Python version: {sys.version}\n")
    f.write(f"Working directory: {sys.path}\n")
    
    try:
        from config import Config
        f.write("Successfully imported Config!\n")
        config = Config()
        f.write(f"API_ID: {config.API_ID}\n")
        f.write(f"API_HASH: {config.API_HASH}\n")
        f.write(f"BOT_TOKEN: {config.BOT_TOKEN}\n")
        f.write(f"MONGO_URL: {config.MONGO_URL}\n")
        f.write(f"LOGGER_ID: {config.LOGGER_ID}\n")
        f.write(f"OWNER_ID: {config.OWNER_ID}\n")
        f.write(f"SESSION1: {config.SESSION1}\n")
        f.write(f"YT_API_KEY: {config.YT_API_KEY}\n")
        f.write(f"YTPROXY_URL: {config.YTPROXY_URL}\n")
        
        try:
            config.check()
            f.write("Config check passed!\n")
        except SystemExit as e:
            f.write(f"Config check failed: {e}\n")
            
    except Exception as e:
        import traceback
        f.write(f"Error: {e}\n")
        f.write(traceback.format_exc())

print("Output written to test_output.txt")
