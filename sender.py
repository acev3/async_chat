import asyncio
from config import CHAT_HOST, SENDER_PORT, ACCOUNT_HASH
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('SENDER')

async def tcp_echo_client(chat_host, chat_port, message):
    reader, writer = await asyncio.open_connection(
            chat_host, chat_port)
    while True:
        response = await reader.readline()
        logger.debug(response)
        logger.debug(f'Send: token')
        token = "{}\n".format(ACCOUNT_HASH)
        writer.write(token.encode("utf-8"))
        await writer.drain()
        response = await reader.readline()
        logger .debug(response)
        await asyncio.sleep(1)
        response = await reader.readline()
        logger.debug(response)
        message = "{}\n".format(message)
        logger.debug(f'Send: {message}')
        await asyncio.sleep(1)
        writer.write(message.encode('utf-8'))
        await writer.drain()
    logger .debug('Close the connection')
    writer.close()


if __name__ == '__main__':
    message = input()
    asyncio.run(tcp_echo_client(CHAT_HOST, SENDER_PORT, message))