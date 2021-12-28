import asyncio
from config import CHAT_HOST, CHAT_PORT


async def tcp_echo_client(host, port):
    print(host)
    reader, writer = await asyncio.open_connection(
        host, port)
    try:
        while True:
            data = await reader.read(100)
            print(f'Received: {data.decode()!r}')
    finally:
        print('Close the connection')
        writer.close()


if __name__ == '__main__':
    asyncio.run(tcp_echo_client(CHAT_HOST, CHAT_PORT))