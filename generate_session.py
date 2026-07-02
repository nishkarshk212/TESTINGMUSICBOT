#!/usr/bin/env python3
from pyrogram import Client
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

async def main():
    print("Generating Pyrogram session string...")
    async with Client(":memory:", api_id=API_ID, api_hash=API_HASH) as app:
        session_string = await app.export_session_string()
        print("\n=== SESSION STRING ===")
        print(session_string)
        print("\n======================")
        
        # Update .env file
        env_path = os.path.join(os.path.dirname(__file__), ".env")
        with open(env_path, "r") as f:
            env_content = f.read()
        
        new_env_content = env_content.replace("SESSION=", f"SESSION={session_string}")
        
        with open(env_path, "w") as f:
            f.write(new_env_content)
        
        print("Session string saved to .env!")

if __name__ == "__main__":
    asyncio.run(main())
