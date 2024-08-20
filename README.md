# lip-python

`lip` is abbreviation for learning in progres.  
Altho I know most of Python features, if not used weekly details are forgotten.  
This is just documentation for myself.

## *args and **kwargs

### args_kwargs.py [code](./args_kwargs.py)
variable positional arguments  
variable keyword arguments  

### args_kwargs_with_functions.py [code](./args_kwargs_with_functions.py)
how to send variable positional arguments and variable keyword arguments to another function 

## dict

### dict.py [code](./dict.py)
dict methods
get -> get value from dict according to key
pop -> get value from dict according to key, but key and value are removed

## same_arguments_to_function.py [code](./same_arguments_to_function.py)
Using one dict for default arguments to function.  
Speed comparison:
- direct call is fastest
- warper is 15% slower than direct call
- `functools.partial` slowest
- dict 10% faster than `functools.partial`

## signals [code](./signals.py)
Example of catching and sending standard UNIX signals to Python program.  
More details at [docs](https://docs.python.org/3/library/signal.html).  
Not available on Windows.  
`CTRL+C` is `SIGINT`.  
`CTRL+Z` is `SIGTSTP`, stop signal generated from keyboard.  
`SIGUSR1` and `SIGUSR2` are signals for user/developer/programer to use in application.  
Use `man 7 signal` for all available signals with names and numbers.  
Use `kill -<signal_name|signal_number> <PID>` for sending signal to process. 

## asyncio

If you plan to use asyncio, than you must not use old booking calls (eg. time.sleep()), but must use new asynchronous coroutines (eg. asyncio.sleep()).

### using_time_sleep [code](./asyncio/001_still_blockin_incorect_use.py)

### using_asyncio_sleep [code](./asyncio/002_fix_for_001.py)

