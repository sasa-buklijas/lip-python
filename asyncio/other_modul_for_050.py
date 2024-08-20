import logging

logger = logging.getLogger(__name__)
#print(f'{__name__=}') # file name without .py when imported. otherwise __main__

def test_log():
    # it is bad practice to call logging.*, line in line below 
    # logging.debug('Logging from other module')
    # because then, how ever is root logger set up it is also this one
    # user have no control
    # better to have separate logger with
    # logger = logging.getLogger(__name__)
    # because than user can configure it 
    # special useful if we need separate log per connection 

    logger.debug('LOGGER from other module')