import logging

def say_hello():
    logging.debug('Hello World, from other_modul.py !')
    #return None

class Dummy():
    def __init__(self):
        logging.debug('__init__ Dummy()')
