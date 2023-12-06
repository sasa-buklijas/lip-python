import os
import signal

def SIGUSR1_handler(signum, frame):
    print('SIGUSR1_handler')
    print(f'{type(signum)=} {type(frame)=}')
    print(f'{signum=} {frame=}')
    print()

def SIGUSR2_handler(signum, frame):
    print('SIGUSR2_handler')
    print(f'{type(signum)=} {type(frame)=}')
    print(f'{signum=} {frame=}')
    print()

def main():
    print(f'{os.getpid()=}')
    # these are signal for developer to use
    signal.signal(signal.SIGUSR1, SIGUSR1_handler)
    signal.signal(signal.SIGUSR2, SIGUSR2_handler)

    while True:
        pass

if __name__ == '__main__':
    main()