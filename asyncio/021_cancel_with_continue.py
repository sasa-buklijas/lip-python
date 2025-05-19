import asyncio
import signal


# idea is that say_hello finis all when shutdown is received
shutdown_event = asyncio.Event()
async def say_hello():

    # same idea, not necessary
    async def is_shutdown_event_set():
        try:
            await shutdown_event.wait()
        except asyncio.CancelledError as e:
            print(f'asyncio.CancelledError received in {asyncio.current_task().get_name()} {e=}')


    while True:
        try:
            shutdown = asyncio.create_task(shutdown_event.wait(), name='shutdown_task')
            #shutdown = asyncio.create_task(is_shutdown_event_set(), name='shutdown_task')
            print_text = asyncio.create_task(asyncio.sleep(0.10), name='print_task')

            done, pending = await asyncio.wait((shutdown, print_text), return_when=asyncio.FIRST_COMPLETED)

            for task in pending:
                task.cancel()

            for task in done:
                # if message is from miner
                if task.get_name() == 'shutdown_task':
                    print('  shutdown_task DONE')
                    return 
                    #await asyncio.sleep(10)
                elif task.get_name() == 'print_task':
                    print('  print_task DONE')
                    print('    B')
                    await asyncio.sleep(5)
                    print('    A')
                else:
                    print(f'UNKNOWN TASK COMPLETED {task.get_name()=} {task=}')

        except asyncio.CancelledError as e:
            # this should not happen
            print(f'say_hello() was cancelled. {shutdown_event.is_set()=} Exiting... {e=}')


async def main():
    asyncio.current_task().set_name('main')
    task = asyncio.create_task(say_hello(), name='say_hello')

    # Wait for the task to complete or be cancelled
    try:
        await task
    except asyncio.CancelledError:
        while pending_tasks:= asyncio.all_tasks():
            len_pending_tasks: int = len(pending_tasks)
            if len_pending_tasks == 1:  # that one task is this task 
                break

            print(f'Waiting on {len_pending_tasks=} tasks: {[t.get_name() for t in pending_tasks]}')
            # await asyncio.sleep is not needed for delay, but for providing loop task switch 
            await asyncio.sleep(0.1)
        # raise needed, for details check comment in redis_main_reader for raise
        raise


if __name__ == "__main__":
    loop = asyncio.new_event_loop()

    def signal_handler(sig_num):
        print(f'{sig_num=} {signal.Signals(sig_num).name=} {signal.strsignal(sig_num)=}')
        #print(f'Number of current async tasks: {len(asyncio.all_tasks(loop))} {asyncio.all_tasks(loop)}')
        print(f'Tasks: {[t.get_name() for t in asyncio.all_tasks(loop)]}')
        print("shutdown_event.set()")
        global shutdown_event
        shutdown_event.set()


    # Attach signal handlers to cancel all tasks
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, signal_handler, sig)

    try:
        loop.run_until_complete(main())
    except asyncio.CancelledError:
        print("asyncio.CancelledError received in __main__")
    finally:
        pending_tasks = asyncio.all_tasks(loop=loop)
        if pending_tasks:
            print(f'Some Tasks left: {pending_tasks=}')
        else:
            print('As expected, all Tasks done.')

        loop.close()
        print("Event loop closed.")
