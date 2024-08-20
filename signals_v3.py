"""Example code for exit signals when work flow is some work and log delay/pause."""
import os
import sys
import time
import signal


class SignalExitManager():
    """Keep state if we are busy and if we received exit signal."""
    def __init__(self):
        self.working = True
        self.exit_signal_received = False
sem = SignalExitManager()


def signal_handler(signum, frame):
    print('signal_handler')
    print(f'{type(signum)=} {type(frame)=}')
    print(f'{signum=} {frame=}')
    #print(f'{dir(signum)=}')
    #print(f'{dir(frame)=}')
    print(f'{signal.Signals(signum).name=} {signal.strsignal(signum)=}')
    global sem
    if sem.working is False:
        print('Exiting from signal_handler.')
        sys.exit(0)
    else:
        print('Can not exit system is still working !')
        sem.exit_signal_received = True


# CTRL+C
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
# SIGKILL, will generate error, because it is not posable to catch:
# The OSError: [Errno 22] Invalid argument occurs because SIGKILL cannot be caught, blocked, or ignored. 
# The same applies to SIGSTOP. These signals are reserved by the operating system for immediate termination and stopping of processes, respectively.
#signal.signal(signal.SIGKILL, signal_handler)


def main():
    global sem
    print(f'{os.getpid()=}')

    while True:
        # simulate work
        sem.working = True
        print('time.sleep 5')
        time.sleep(5)
        sem.working = False

        # check if exit signal was received
        if sem.exit_signal_received:
            print(f'{sem.exit_signal_received=} exiting.')
            sys.exit(0)

        # simulate pause
        print('Now is 20 second wait/pause.')
        time.sleep(20)


if __name__ == '__main__':
    main()
