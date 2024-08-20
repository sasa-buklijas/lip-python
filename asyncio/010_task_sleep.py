# SuperFastPython.com
# example of scheduling an async task
import asyncio

# coroutine to perform some useful task
async def task_coro():
	# report a message
	print('The task is running...')
	# suspend and sleep for a moment
	await asyncio.sleep(1)
	# report a message
	print('The task done')
	# return a result
	return 'The answer is 100'

# main coroutine
async def main():
	t1 = asyncio.create_task(asyncio.sleep(0.10), name='t1')
	t2 = asyncio.create_task(asyncio.sleep(0.5), name='t2')
	tasks = [t1, t2]

	# Wait for first completed task
	done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

	# Cancel the pending tasks, must se done this way, there is no was to pause task
	for task in pending:
		task.cancel()
	await asyncio.gather(*pending, return_exceptions=True)

	for task in done:
		if task.get_name() == 't1':
			print('t1 done.')
		elif task.get_name() == 't2':
			print('t2 done.')
		else:
			print('unknown done.')

if __name__ == '__main__':
    # create the coroutine and run it in the event loop
    asyncio.run(main())