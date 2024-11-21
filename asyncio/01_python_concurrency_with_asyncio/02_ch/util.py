import asyncio

async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} second(s)')
    return delay_seconds


async def delay_1(delay_seconds: int) -> int:
    try:
        print(f'sleeping for {delay_seconds} second(s)')
        await asyncio.sleep(delay_seconds)
        print(f'finished sleeping for {delay_seconds} second(s)')
        return delay_seconds
    except asyncio.CancelledError:
        print('delay_1 was cancelled')


async def delay_2(delay_seconds: int) -> int:
    try:
        print(f'sleeping for {delay_seconds} second(s)')
        await asyncio.sleep(delay_seconds)
        print(f'finished sleeping for {delay_seconds} second(s)')
        return delay_seconds
    except asyncio.CancelledError as e:
        print('delay_1 was cancelled')
        raise e
        #raise ValueError('NOT A NUMBER')
