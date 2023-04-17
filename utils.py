from datetime import datetime

import click


def time_it(f):
    async def _inner(*args, **kwargs):
        start = datetime.now()
        result = await f(*args, **kwargs)
        click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
        return result
    return _inner
