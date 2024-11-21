import asyncio
from util import delay

async def main():
    # take 6 seconds, 2*3=6    
    print("a")
    await delay(2)
    print("b")
    await delay(2)
    print("c")
    await delay(2)
    print("d")

asyncio.run(main())