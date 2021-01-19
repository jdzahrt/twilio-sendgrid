import aiohttp
import asyncio
from dotenv import load_dotenv
import os

tok = load_dotenv('.env')

async def main():
    async with aiohttp.ClientSession(headers={'authorization': f"Bearer {os.environ.get('SENDGRID_TOKEN')}"}) as session:
        async with session.get(
                'https://api.sendgrid.com/v3/stats?aggregated_by=day&start_date=2021-01-19&end_date=2021-01-19') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            json = await response.json()
            print(json[0])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
