

def generator_function_no_return():
    yield 1
    yield 2

def generator_function_with_return():
    yield 1
    yield 2
    return 5


def main():
    this_is_generator = generator_function_no_return()
    print(this_is_generator)    # <generator object generator_function_no_return at 0x1023809e0>
    print(next(this_is_generator))  # 1
    print(next(this_is_generator))  # 2
    #print(next(this_is_generator))  # StopIteration

    #print(next(this_is_generator))  # StopIteration
    # no need to catch  exception
    for i in generator_function_no_return():
        print(i)

    #
    # generator_function_with_return()
    #

    print('generator_function_with_return()')
    for i in generator_function_with_return():
        print(i) # 1 an 2, no 5

    # to get return fro generator 
    # only way is to get catch StopIteration exception manually
    gen = generator_function_with_return()
    while True:
        try:
            value = next(gen)
            print("Yielded:", value)
        except StopIteration as e:
            print("Returned:", e.value)  # This will be 5
            break

    # from chatGTP, but hallucination, because result is None
    print('fro chatGTP, but hallucination ')
    gen = generator_function_with_return()
    for value in gen:
        print("Yielded:", value)
    try:
        next(gen)
    except StopIteration as e:
        print("Returned:", e.value)  # This will be 5

if __name__ == "__main__":
    main()
