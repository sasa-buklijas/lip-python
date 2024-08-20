import asyncio 

async def q():
    print("Why can't programmers tell jokes?")
    #await asyncio.sleep(1)

async def a():
    print("Timing!")

async def main():
    #await asyncio.gather(q(), a())
    await asyncio.gather(*[q(), a()])
    # not sure but it look like it is always, first run first 

asyncio.run(main())