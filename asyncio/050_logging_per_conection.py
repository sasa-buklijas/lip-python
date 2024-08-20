import asyncio
from asyncio import StreamReader, StreamWriter
from contextlib import suppress
import logging
import signal
from other_modul_for_050 import test_log

# send messages with nc localhost 8888

async def echo(reader: StreamReader, writer: StreamWriter): 
    peername = writer.get_extra_info('peername')

    connection_id = f"{peername[0]}_{peername[1]}"  # Using peername as connection ID

    # How to change task name
    # Get the current task
    task = asyncio.current_task()
    # Change the task's name
    task.set_name(connection_id)

    #logger = logging.getLogger(connection_id)  #
    #logger.addHandler(logging.FileHandler(f'connection_{connection_id}.log'))

    logger = logging.getLogger(connection_id)
    handler = logging.FileHandler(f'connection_{connection_id}.log')
    # formatter = logging.Formatter('%(asctime)s:%(msecs)03d:%(filename)s:%(lineno)5d:%(levelname)10s:%(name)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_formatter = root_logger.handlers[0].formatter
    handler.setFormatter(root_formatter)
    logger.addHandler(handler)

    # CAUTION, if other_modul_for_050 is already disabled, that this will not work
        # because it si already disabled
    # this will take logger from module test_log
    #xl = logging.getLogger('other_modul_for_050')
    # this is dynamic way
    xl = logging.getLogger(test_log.__module__)
    #print(f'{test_log.__module__=}')
    # and add it to log file of each connection
    xl.addHandler(handler)

    #
    #logger.propagate = False

    #logging.info(f'New connection from {peername}.')
    logger.info(f'New connection from {peername}.')
    try:
        while data := await reader.readline(): 
            #logging.info(f'Received data {data=}')
            logger.info(f'Received data {data=}')
            data = data.decode()
            test_log() # Just to test what logger is it using (it is using default)
            writer.write(f'Return as uppercase:{data.upper()}'.encode())
            await writer.drain()
            #logging.info('Uppercase data send back')
            logger.info(f'Received data {data=}')
        #logging.info('Leaving Connection.') 
        logger.info(f'Received data {data=}')
    except asyncio.CancelledError:
        #logging.info('Connection dropped!')
        logger.info(f'Received data {data=}')


async def main(host='127.0.0.1', port=8888):
    logging.info(f'Listening on {host}:{port}')
    server = await asyncio.start_server(echo, host, port)
    async with server:

        # Catch SIGINT and SIGTERM signals
        # for sig_name in ('SIGINT', 'SIGTERM'):
        #     asyncio.get_running_loop().add_signal_handler(
        #         getattr(signal, sig_name),
        #         lambda sig_name=sig_name: asyncio.create_task(shutdown(sig_name, server))
        #     )

        # old way, only this
        await server.serve_forever()

        # not so good
        #with suppress(asyncio.CancelledError):
        #    await server.serve_forever()

        # with this no exceptions
        #try:
        #    await server.serve_forever()
        #except asyncio.CancelledError:
        #    pass


async def shutdown(sig_name, server):
    logging.info(f'Received {sig_name}. Shutting down gracefully...')
    server.close()
    await server.wait_closed()
    logging.info('Server closed')


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        #format='%(asctime)s:%(msecs)03d:%(filename)s:%(lineno)5d:%(levelname)10s:%(name)s:%(message)s',
        # not much use of %(taskName)s if it is random generated
        # but it is fine if it is set to something useful full
        format='%(asctime)s:%(msecs)03d:%(taskName)s:%(filename)s:%(lineno)5d:%(levelname)10s:%(name)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler('connections_all.log'),
            logging.StreamHandler()
        ]
    )

    # this will disable all logs from other_modul_for_050 module
    # even if we add handler, record, etc, later
    #logging.getLogger('other_modul_for_050').disabled = True

    try: 
        asyncio.run(main())
    except KeyboardInterrupt: 
        logging.info('Bye!')
