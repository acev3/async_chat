import asyncio
from config import CHAT_HOST, CHAT_PORT, HISTORY_PATH
import datetime
import aiofiles
import argparse


async def tcp_echo_client(host, port, filepath):
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
            async with aiofiles.open(filepath, mode='a') as f:
                await f.write(message)
    finally:
        print('Close the connection')
        writer.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, help='Set host')
    parser.add_argument('--port', type=int, help='Set port')
    parser.add_argument(
        '--history',
        type=str,
        help='Set history path',
    )
    args = parser.parse_args()

    chat_host =  args.host or CHAT_HOST
    chat_port = args.port or CHAT_PORT
    history_path = args.history or HISTORY_PATH
    asyncio.run(tcp_echo_client(chat_host, chat_port, history_path))