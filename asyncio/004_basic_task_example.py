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
	# run a task independently
	task = asyncio.create_task(task_coro())
	# suspend a moment, allow the scheduled task to run
	await asyncio.sleep(0)

	# check if the task is done
	if task.done():
		# get the return value
		value = task.result()
		print(f'Task done {value=}.')
	else:
		print('Task still not done.')

	# wait for the async task to complete
	await task

	# check if the task is done
	if task.done():
		# get the return value
		value = task.result()
		print(f'Task done {value=}.')

	# report the return value
	print(f'Got: {task.result()}')

if __name__ == '__main__':
    # create the coroutine and run it in the event loop
    asyncio.run(main())