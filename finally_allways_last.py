# finally can be used in function for closing resurse
# it will be called in the end even if there is uncaught exception 

def t1():
    try:
        print('T1 In Try.')
    finally:
        print('T1 finally')


def t2():
    try:
        print('T2 In Try, exception next')
        _ = 2 / 0    # ZeroDivisionError
        # it will be showed on screen after print('T2 finally')
    finally:
        print('T2 finally')


def t3():
    try:
        print('T3 In Try, exception next')
        _ = 2 / 0    # ZeroDivisionError
    except ZeroDivisionError as e:
        print(f'T2 catches ZeroDivisionError  {e=}')
        #raise e    print('T3 finally') always, even with "raise e" 
    finally:
        print('T3 finally')


def main():
    t1()
    print()

    t3()
    print()

    # t2 is last because its exception is not catch, so main will stop   
    t2()
    print()


if __name__ == "__main__":
    main()
