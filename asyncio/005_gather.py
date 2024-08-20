# SuperFastPython.com
# example of running many coroutines concurrently
import random
import asyncio

# coroutine to perform some useful task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random.random()
    # suspend and sleep for a moment
    #await asyncio.sleep(value)
    # report the argument and value
    print(f'Task {arg:2} done after {value:1.9f} seconds')
    return arg 

# main coroutine
async def main():
    # create many coroutines
    coros = [task_coro(i) for i in range(100)]
    # run all coroutines
    # it is race/random which coroutine will rune first, because of sleep inside coroutine
    result1 = await asyncio.gather(*coros)
    # but results will be sorted by Task Number
    print(result1)

# create the coroutine
# ine and run it in the event loop
asyncio.run(main())