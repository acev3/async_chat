import asyncio
from config import CHAT_HOST, CHAT_PORT, HISTORY_PATH
import datetime
import aiofiles
import argparse
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('lISTENER')


async def listen_chat(host, port, filepath):
    reader, writer = await asyncio.open_connection(
        host, port)
    try:
        while True:
            data = await reader.readline()
            now = datetime.datetime.now()
            formatted_date = now.strftime('%d.%m.%Y %H:%M')
            message = f'[{formatted_date}] {data.decode("utf-8")}'
            logger.debug(message)
            async with aiofiles.open(filepath, mode='a') as f:
                await f.write(message)
    finally:
        logger.debug('Close the connection')
        writer.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, help='Set host', default=CHAT_HOST)
    parser.add_argument('--port', type=int, help='Set port', default=CHAT_PORT)
    parser.add_argument('--history', type=str, help='Set history path', default=HISTORY_PATH)
    args = parser.parse_args()
    chat_host =  args.host
    chat_port = args.port
    history_path = args.history
    asyncio.run(listen_chat(chat_host, chat_port, history_path))