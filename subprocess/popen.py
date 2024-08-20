import subprocess
import random
import time

r = random.randint(1, 1000000000)
new_file = f'file_{r}.txt'
print(f'will make file {new_file}')
time.sleep(1)

command = ["./t.sh", new_file]

process = subprocess.Popen(command)

subprocess_pid = process.pid

#print(f'{dir(process)=}')
print(f'Python done, but shell {subprocess_pid} is still running.')
