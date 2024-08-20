import asyncio

# generator
def odds(start: int, stop: int):
    for odd in range(start, stop+1, 2):
        yield odd

# define a coroutine, asynchronous generator
    # because it have yield in it
async def square_odds(start: int, stop: int):
    for odd in odds(start, stop):  
        await asyncio.sleep(2)
        yield odd ** 2
    
async def main():
    async for so in square_odds(11, 17):
        print('so', so)

if __name__ == '__main__':
    asyncio.run(main())
