
def test_1(*args, **kwargs):
    print(f'test_1 {args=} {type(args)=}')     # variable positional arguments 
    print(f'test_1 {kwargs=} {type(kwargs)=}') # variable keyword arguments
    print()


def main():
    test_1()
    #args=() type(args)=<class 'tuple'>
    #kwargs={} type(kwargs)=<class 'dict'>
    
    test_1(1, 'a')      # o to n
    # args=(1, 'a') type(args)=<class 'tuple'>
    # kwargs={} type(kwargs)=<class 'dict'>

    test_1(a=1, b='a')  # o to n
    #args=() type(args)=<class 'tuple'>
    #kwargs={'a': 1, 'b': 'a'} type(kwargs)=<class 'dict'>

    test_1(1, 'a', a=1, b='a')  # together
    # args=(1, 'a') type(args)=<class 'tuple'>
    # kwargs={'a': 1, 'b': 'a'} type(kwargs)=<class 'dict'>


if __name__ == "__main__":
    main()