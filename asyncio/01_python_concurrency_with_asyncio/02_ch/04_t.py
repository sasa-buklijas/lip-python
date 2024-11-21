import asyncio
from asyncio import CancelledError
from util import delay_2


async def main():
    long_task = asyncio.create_task(delay_2(1))

    seconds_elapsed = 0

    try:
        while not long_task.done():
            print('Task not finished, checking again in a second.')
            await asyncio.sleep(1)
            seconds_elapsed = seconds_elapsed + 1
            if seconds_elapsed == 5:
                long_task.cancel()
                # asyncio.sleep(1) one will not raise exception from long_task Task
                #await asyncio.sleep(1)
                # for delay will raise exception
                # for delay_1 will raise exception, because exception is catched in delay_1
                # for delay_2 will raise exception
                await long_task

    except CancelledError:
    #except BaseException:
        # this will still not happen
        print('Our task was cancelled IN LOOP')


    print('A')
    try:
        # for delay will raise exception, again
        # for delay_1 will raise exception, because exception is catched in delay_1
        # for delay_2 will raise exception again 
        r = await long_task
        print(f'Return fo await long_task: {r=}')
    except CancelledError:
        print('Our task was cancelled')
    # if I delete it, then next r = await long_task will not work
    #del long_task

    # Conclusion
    # if exception was not catched in Task 
    # it is raised every time when Task is await
    # look like that is for every exception 
    try:
        r = await long_task
        print(f'Return fo await long_task: {r=}')
    except CancelledError:
        print('Our task was cancelled. Third time')

asyncio.run(main())