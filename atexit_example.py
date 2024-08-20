import atexit
# useful for function to be run on program exit 

def c1():
    print('C1 def')

def t2():
    try:
        print('T2 In Try, exception next')
        _ = 2 / 0    # ZeroDivisionError
        # it will be showed on screen after print('T2 finally')
    finally:
        print('T2 finally')

def c3():
    print('C3 def')

# decorator can be used also
@atexit.register
def c4():
    print('C4 def')

# multiple functions can be registered here...    
#atexit.register(c1)
#atexit.register(c3)

atexit.register(c3)
atexit.register(c1) # this one will be called first, like LIFO

def main():
    print('main')
    t2()

if __name__ == "__main__":
    main()
