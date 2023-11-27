from functools import partial
import time

def lot_of_arguments(a: int, b: int, c: int, d: int, e: int, f: int):
    return a+b+c+d+e+f

def main():
    number_of_iterations = 2500

    # givin default argument
    # it is tidies when function call is called in multiple time
    # if parameters change it easy to forget to chang it in all places
    t1 = time.perf_counter_ns()
    for i in range(number_of_iterations):
        lot_of_arguments(i, 11, 22, 33, 44, 55)
    print(f'Arguments {(time.perf_counter_ns() - t1) / 1_000_000_000} seconds')

    # make dict with default arguments
    # easy to change
    t1 = time.perf_counter_ns()
    default_for_lot_of_arguments = {'b':11, 'c':22, 'd':33, 'e':44, 'f':55}
    for i in range(number_of_iterations):
        lot_of_arguments(i, **default_for_lot_of_arguments)
    print(f'Dict      {(time.perf_counter_ns() - t1) / 1_000_000_000} seconds')

    # you can also make partial function
    # is is useful if you will never change them 
    t1 = time.perf_counter_ns()
    g = partial(lot_of_arguments, b=11, c=22, d=33, e=44, f=55)
    for i in range(number_of_iterations):
        g(i)
    print(f'Partial   {(time.perf_counter_ns() - t1) / 1_000_000_000} seconds')

    # same as partial, but write more code 
    t1 = time.perf_counter_ns()
    def g(i):
        lot_of_arguments(i, 11, 22, 33, 44, 55)
    for i in range(number_of_iterations):
        g(i)
    print(f'Warper    {(time.perf_counter_ns() - t1) / 1_000_000_000} seconds')


if __name__ == "__main__":
    main()