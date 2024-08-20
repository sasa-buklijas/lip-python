import os
import sys
import time
import signal

exit_main = False
def signal_handler(signum, frame):
    print('signal_handler')
    print(f'{type(signum)=} {type(frame)=}')
    print(f'{signum=} {frame=}')
    #print(f'{dir(signum)=}')
    #print(f'{dir(frame)=}')
    print(f'{signal.Signals(signum).name=} {signal.strsignal(signum)=}')
    print()
    if signal.Signals(signum).name != 'SIGTERM':
        global exit_main    # global exit_main is mandatory
        exit_main = True
    else:
        print('ignoring SIGTERM, when will OS stop process.')
    #sys.exit(0)

# CTRL+C
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
# SIGKILL, will generate error, because it is not posable to catch:
# The OSError: [Errno 22] Invalid argument occurs because SIGKILL cannot be caught, blocked, or ignored. 
# The same applies to SIGSTOP. These signals are reserved by the operating system for immediate termination and stopping of processes, respectively.
#signal.signal(signal.SIGKILL, signal_handler)


def main():
    global exit_main
    print(f'{os.getpid()=}')

    # try:
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     # This will also handle Ctrl+C gracefully
    #     print('\nKeyboardInterrupt received, exiting...')
    #     exit(0)

    while True:
        pass

        if exit_main:
            print(f'{exit_main=}')
            sys.exit(0)
        
        print('time.sleep 10')
        time.sleep(10)


if __name__ == '__main__':
    main()
