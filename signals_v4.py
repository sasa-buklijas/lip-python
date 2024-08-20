""" Example code for exit signals when work flow is some work and log delay/pause.
    Same as signals_v3.py, but no global variables, signal_handler in class.  
"""
import os
import sys
import time
import signal


class SignalHandler:
    def __init__(self):
        self.allow_exit = False
        self.exit_signal_received = False

    def handle_signal(self, signum, frame):
        print(f'{signal.Signals(signum).name=} {signal.strsignal(signum)=}')
        if self.allow_exit:
            print('Exiting from signal_handler.')
            sys.exit(0)
        else:
            print('Can not exit system is still working !')
            self.exit_signal_received = True


def main():
    #time.sleep(10)     # if uncommented and we got signal to exit it will exit immediately
    print(f'{os.getpid()=}')

    signal_handler = SignalHandler()
    signal.signal(signal.SIGINT, signal_handler.handle_signal)  # CTRL+C
    signal.signal(signal.SIGTERM, signal_handler.handle_signal)


    while True:
        # simulate work
        signal_handler.allow_exit = False
        print('time.sleep 5')
        time.sleep(5)
        signal_handler.allow_exit = True

        # check if exit signal was received
        if signal_handler.exit_signal_received:
            print(f'{signal_handler.exit_signal_received=} exiting.')
            sys.exit(0)

        # simulate pause
        print('Now is 20 second wait/pause.')
        time.sleep(20)


if __name__ == '__main__':
    main()
