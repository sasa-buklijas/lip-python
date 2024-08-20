# SuperFastPython.com
# example of waiting for a collection of tasks
import random
import asyncio

# coroutine to perform some useful task
async def task_coro(arg):
	# generate a random value between 0 and 1
	value = random.random()
	# suspend and sleep for a moment
	await asyncio.sleep(value)
	# return a value unique for this task
	return arg #* value

# main coroutine
async def main():
	#for i in range(100):
	#	print(i)

	# create and schedule many independent tasks
	tasks = [asyncio.create_task(task_coro(i)) for i in range(100)]
	# The first task is assigned the name "Task-2" because the default naming starts from 2. 
	# This is done to avoid conflicts with the default loop's internal task, 
	# which is assigned the name "Task-1".

	# If you want to customize the task name, you can pass the name parameter to asyncio.create_task:
	### tasks = [asyncio.create_task(task_coro(i), name=f'MyTask-{i}') for i in range(100)]
	
	# just for checking names of tasks
	#for task in tasks:
	#	print(f'{task.get_name()=}')

	# suspend and wait for the first task to complete
	done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

	# report the result from the first task
	task = done.pop()
	print(f'First Task {task.get_name()} got: {task.result()}\n')
	# if we do not do await asyncio.wait(pending,
	# program stops

	# wait for the rest of the tasks to complete
	remaining_done, _ = await asyncio.wait(pending, return_when=asyncio.ALL_COMPLETED)

    # report the result from all tasks
	for task in remaining_done:
		print(f'Task {task.get_name()} got: {task.result()}')

# create the coroutine and run it in the event loop
asyncio.run(main())
