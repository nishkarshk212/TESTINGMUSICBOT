import asyncio
import aiohttp

API_URL = "http://rg3jvd5nx24fip69wgz54vgv.45.76.155.143.sslip.io"
API_KEY = "NISHKARSH_eTKQjVzWOQEB6aploRZ@r)X1A4(r)MC1"
VIDEO_ID = "NgjERPTaC4Y"

async def test_api():
    headers = {"X-API-Key": API_KEY}
    
    print(f"Testing {API_URL}/health...")
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/health", headers=headers) as resp:
            print(f"Health status: {resp.status}")
            print(await resp.text())
        
        print(f"\nTesting {API_URL}/audio with id={VIDEO_ID}...")
        async with session.get(
            f"{API_URL}/audio",
            headers=headers,
            params={"id": VIDEO_ID, "platform": "youtube"}
        ) as resp:
            print(f"Audio status: {resp.status}")
            print(await resp.text())

asyncio.run(test_api())
