import asyncio
from datetime import datetime

from utils import time_it

start = datetime.now().second


async def sleep_and_print(seconds):
    print(f"{datetime.now().second - start} starting {seconds} sleep 😴")
    await asyncio.sleep(seconds)
    print(f"{datetime.now().second - start} finished {seconds} sleep ⏰")

    return seconds


async def sleep(seconds):
    print(f"{datetime.now().second - start} starting {seconds} sleep 😴")
    await asyncio.sleep(seconds)
    await sleep_and_print(5)
    print(f"{datetime.now().second - start} finished {seconds + 5} sleep ⏰")

    return seconds + 5


@time_it
async def main():
    coroutines = [sleep(3), sleep_and_print(5)]
    results = await asyncio.gather(*coroutines)
    print(results)


if __name__ == '__main__':
    asyncio.run(main())

