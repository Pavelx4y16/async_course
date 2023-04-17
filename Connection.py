from my_decors import b_print
import asyncio
from aiohttp import ClientSession
import requests


class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # async def __aenter__(self):
    #     return await self.get_connection()

    def __enter__(self):
        return self

    # async def __aexit__(self, exc_type, exc_val, exc_tb):
    #     return await self.close()
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    async def put_data(self):
        b_print(f'Putting data to some Remote DB...')
        await asyncio.sleep(2)
        b_print(f'(Put) Succeed')

    async def get_weather(self, city):
        b_print(f'Getting weather for {city}...')
        async with ClientSession() as session:
            params = {
                'q': city,
                'APPID': self.port
            }
            async with session.get(url=self.host, params=params) as resp:
                weather_json = await resp.json()
                return f'{city}: {weather_json["weather"][0]["main"]}'

    def get_sync_weather(self, city):
        params = {
            'q': city,
            'APPID': self.port
        }
        weather_json = requests.get(url=self.host, params=params).json()
        b_print(f'{city}: {weather_json["weather"][0]["main"]}')

    async def close(self):
        b_print(f'Closing connection...')
        await asyncio.sleep(1)
        b_print(f'(Close) Succeed')

    async def get_connection(self):
        # b_print(f'Getting connection...')
        # await asyncio.sleep(1)
        # b_print(f'(get conn) Succeed')

        return self
