import asyncio
import time

# define a coroutine
async def custom_coro(msg: str, sn: int):
    # this is problem
    # using time.sleep and it is blocking
    time.sleep(sn)
    print(f'Hello there {msg}')

async def main():
    # this is just calling one after the other
    #await custom_coro('first', 3)
    #await custom_coro('second', 2)
    #await custom_coro('third', 1)

    # this will start them in same time
    await asyncio.gather(
        custom_coro('first', 3),
        custom_coro('second', 2),
        custom_coro('third', 1)
    )

if __name__ == '__main__':
    asyncio.run(main())
