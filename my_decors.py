from datetime import datetime


def time(f):
    def inner(*args, **kwargs):
        start = datetime.now()
        res = f(*args, **kwargs)
        finish = datetime.now()
        print(f'Execution time: {finish - start}')
        return res
    return inner


def async_time(f):
    async def inner(*args, **kwargs):
        start = datetime.now()
        res = await f(*args, **kwargs)
        finish = datetime.now()
        print(f'Execution time: {finish - start}')

        return res
    return inner


def b_print(msg):
    print(f'{datetime.now():%S.%f}::::{msg}')
