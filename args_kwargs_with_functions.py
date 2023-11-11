def test_2(first, *args, **kwargs):
    print(f'test_2 {first=} {type(first)=}')
    print(f'test_2 {args=} {type(args)=}')  # first is consumed   
    print(f'test_2 {kwargs=} {type(kwargs)=}') 
    print()
    test_3(*args, **kwargs)     # send rest to another function

def test_3(a=None, *args, **kwargs):
    print(f'test_3 {a=} {type(a)=}')
    print(f'test_3 {args=} {type(args)=}')     
    print(f'test_3 {kwargs=} {type(kwargs)=}') 
    print()

def main():
    test_2(1, a='a', b='b') 
    
    #test_2(1, 2, a='a', b='b')
    # will not work, because there are multiple values for argument 'a'
    # is test_3 a 2 or 'a'

    #test_3(1, 2, a='a', b='b')
    # will not work, because there are multiple values for argument 'a'
    # is test_3 a 1 or 'a'
    
    test_3(1, 2, c=1, b='a') 
    # in test_3 a is 1


if __name__ == "__main__":
    main()