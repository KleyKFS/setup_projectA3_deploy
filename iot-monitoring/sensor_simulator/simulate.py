import asyncio
import random
import aiohttp

URL = "https://a3-deploy.onrender.com/data"

async def send_data(sensor_id):
    while True:
        data = {
            "sensor_id": sensor_id,
            "temperature": round(random.uniform(20, 35), 2),
            "humidity": round(random.uniform(30, 70), 2)
        }
        async with aiohttp.ClientSession() as session:
            await session.post(URL, json=data)
        await asyncio.sleep(5)

async def main():
    tasks = [send_data(f"sensor_{i}") for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
