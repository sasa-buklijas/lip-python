import asyncio
import signal


# This will not close/cancel this Task, because there is no raise
# but it will not do print("After  sleep"), so no continue
# but will start from beginning
async def say_hello():
    while True:
        try:
            print("Before sleep")
            await asyncio.sleep(5)
            print("After  sleep")
        except asyncio.CancelledError:
            print("say_hello() was cancelled. Exiting...")
            #raise  # if commented, endless loop


async def main():
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
        print(f'Number of current async tasks: {len(asyncio.all_tasks(loop))}')
        print("\nReceived stop signal. Cancelling tasks...")
        for task in asyncio.all_tasks(loop):
            task_name = task.get_name()
            print(f'START send task.cancel() to {task_name}')
            rv = task.cancel('SIGNAL_HANDLER_MSG')
            print(f'END   send task.cancel() to {task_name} {rv}')

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
