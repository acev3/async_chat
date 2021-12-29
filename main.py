import asyncio
from config import CHAT_HOST, CHAT_PORT
import datetime
import aiofiles


async def tcp_echo_client(host, port):
    print(host)
    reader, writer = await asyncio.open_connection(
        host, port)
    try:
        while True:
            data = await reader.read(100)
            now = datetime.datetime.now()
            formatted_date = now.strftime("%d.%m.%Y %H:%M")
            message = f'[{formatted_date}] {data.decode()!r}'
            print(message)
            async with aiofiles.open('test.txt', mode='a') as f:
                await f.write(message)
    finally:
        print('Close the connection')
        writer.close()


if __name__ == '__main__':
    asyncio.run(tcp_echo_client(CHAT_HOST, CHAT_PORT))