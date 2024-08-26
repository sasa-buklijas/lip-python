import asyncio
from asyncio import StreamReader, StreamWriter

# send messages with nc localhost 7000
async def echo(reader: StreamReader, writer: StreamWriter): 
    peername = writer.get_extra_info('peername')
    connection_id = f"{peername[0]}:{peername[1]}"  # Using peername as connection ID
    print(f'Open connection to {connection_id=}')

    while data := await reader.readline():
        print(f'Received data {data=}')
        data = data.decode()
        writer.write(f'Return as uppercase:{data.upper()}'.encode())
        await writer.drain()


async def main(host='127.0.0.1', port=7000):
    print(f'Server running on {host}:{port}')
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
