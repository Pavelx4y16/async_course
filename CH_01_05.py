import asyncio
from datetime import datetime
import click


async def sleep_five():
    print(f"start sleeping for 5 seconds...")
    await asyncio.sleep(5)
    print(f"finishing sleeping for 5 seconds...")

    return 5


async def sleep_three_then_five():
    print(f"start sleeping for 3 seconds...")
    await asyncio.sleep(3)
    print(f"finishing sleeping for 3 seconds...")
    await sleep_five()

    return 3


async def main():
    results = await asyncio.gather(sleep_five(), sleep_three_then_five())
    print(results)


if __name__ == '__main__':
    start = datetime.now()
    asyncio.run(main())
    click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
