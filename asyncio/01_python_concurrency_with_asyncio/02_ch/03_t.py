import asyncio
from asyncio import CancelledError
from util import delay


async def main():
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print('Task not finished, checking again in a second.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            # cancel() will change long_task status to done
            long_task.cancel()  
        print(long_task.done())

    print('A')
    try:
        pass
        # asyncio.sleep(1) one will not raise exception from long_task Task
        #await asyncio.sleep(1)
        # await will return return_value in Task or if Exception exist in Task raise it
        r = await long_task
        print(f'Return fo await long_task: {r=}')
    except CancelledError:
        # from util import delay_1 
        # delay_1 will not generate print because exception is catched in delay_1
        # from util import delay_2
        # delay_1 will generate print because exception is raised again in delay_2
        print('Our task was cancelled')

asyncio.run(main())