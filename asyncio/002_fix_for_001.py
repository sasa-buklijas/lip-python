import asyncio

# define a coroutine
async def custom_coro(msg: str, sn: int):
    await asyncio.sleep(sn)
    print(f'Hello there {msg}')

async def main():
    #await custom_coro('first', 3)
    #await custom_coro('second', 2)
    #await custom_coro('third', 1)   

    # FIRST SOLUTION
    # this will start them in same time
    await asyncio.gather(
        custom_coro('first', 3),
        custom_coro('second', 2),
        custom_coro('third', 1)
    )
    print()

    # SECOND SOLUTION
    # Create tasks for each coroutine
    task1 = asyncio.create_task(custom_coro('first', 3))
    task2 = asyncio.create_task(custom_coro('second', 2))
    task3 = asyncio.create_task(custom_coro('third', 1))
    # Wait for all tasks to complete
    await asyncio.gather(task1, task2, task3)

if __name__ == '__main__':
    asyncio.run(main())
