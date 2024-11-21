import asyncio
from util import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(2))
    sleep_again = asyncio.create_task(delay(2))
    sleep_once_more = asyncio.create_task(delay(2))
    
    # if uncommented task will start here, need await
    #await asyncio.sleep(0)

    # take 2 seconds
    print("a")
    await sleep_for_three
    # after this all task are starting, because of await
    print("b")
    await sleep_again
    print("c")
    await sleep_once_more
    print("d")

asyncio.run(main())