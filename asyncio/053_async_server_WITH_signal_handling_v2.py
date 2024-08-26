import signal
import asyncio
from asyncio import StreamReader, StreamWriter

# send messages with nc localhost 7000
async def echo(reader: StreamReader, writer: StreamWriter): 
    peername = writer.get_extra_info('peername')
    connection_id = f"{peername[0]}:{peername[1]}"  # Using peername as connection ID
    print(f'Open connection to {connection_id=}')

    # while data := await reader.readline():
    #     print(f'Received data {data=}')
    #     data = data.decode()
    #     writer.write(f'Return as uppercase:{data.upper()}'.encode())
    #     await writer.drain()

    try:
        while data := await reader.readline():
            print(f'Received data {data=}')
            data = data.decode()
            writer.write(f'Return as uppercase: {data.upper()}'.encode())
            await writer.drain()
    except asyncio.CancelledError:
        print(f'Connection {connection_id} canceled')
        raise  # Allow the cancellation to propagate
    finally:
        print(f'Closing connection to {connection_id}')
        writer.close()
        await writer.wait_closed()


async def main(host='127.0.0.1', port=7000):
    print(f'Server running on {host}:{port}')
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


def signal_handler(loop):
    """ Signal handler for stopping the event loop gracefully. """
    for task in asyncio.all_tasks(loop):
        print(f'START send task.cancel() to\n{task=}')
        task.cancel()
        print(f'END   send task.cancel() to\n{task=}')
    loop.stop()


if __name__ == "__main__":
    #asyncio.run(main())

    #loop = asyncio.get_event_loop()

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # No running loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Register signal handlers
    loop.add_signal_handler(signal.SIGINT, signal_handler, loop)
    loop.add_signal_handler(signal.SIGTERM, signal_handler, loop)

    try:
        loop.run_until_complete(main())
    except asyncio.CancelledError:
        pass
    finally:
        loop.close()
        print("Server stopped gracefully.")
