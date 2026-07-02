
import yt_dlp
import os

ydl_opts = {
    "quiet": False,
    "no_warnings": False,
    "cookiefile": os.path.join(os.path.dirname(__file__), "app", "cookies.txt"),
}

print("Testing yt-dlp...")

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info("YQHsXMglC9A", download=False)
        print(f"Successfully got info for {info.get('title')}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    print(traceback.format_exc())

print("\nTrying without cookies...")
ydl_opts_no_cookies = ydl_opts.copy()
if "cookiefile" in ydl_opts_no_cookies:
    del ydl_opts_no_cookies["cookiefile"]

try:
    with yt_dlp.YoutubeDL(ydl_opts_no_cookies) as ydl:
        info = ydl.extract_info("YQHsXMglC9A", download=False)
        print(f"Successfully got info for {info.get('title')}")
except Exception as e:
    print(f"Error without cookies: {e}")
    import traceback
    print(traceback.format_exc())
