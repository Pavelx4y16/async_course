import asyncio
from Connection import Connection
from my_decors import async_time, time

CITIES = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York', 'Gomel'] * 10
HOST = 'http://api.openweathermap.org/data/2.5/weather'
PORT = '360bc0897a7a4be3e0fa60ad79c948ca'


@async_time
async def async_main():
    with Connection(host=HOST, port=PORT) as conn:
        tasks = [asyncio.create_task(conn.get_weather(city)) for city in CITIES]
        res = await asyncio.gather(*tasks)
        for weather in res:
            print(weather)


@time
def sync_main():
    with Connection(host=HOST, port=PORT) as conn:
        for city in CITIES:
            conn.get_sync_weather(city)


if __name__ == '__main__':
    print('Running Async...')
    asyncio.run(async_main())

    # print('\n\nRunning the same but with Sync')
    # sync_main()

