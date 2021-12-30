import asyncio
from config import CHAT_HOST, SENDER_PORT, ACCOUNT_HASH
import logging
import json


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('SENDER')

async def tcp_echo_client(chat_host, chat_port, message):
    ACCOUNT_HASH = '123'
    reader, writer = await asyncio.open_connection(
            chat_host, chat_port)
    response = await reader.readline()
    logger.debug(response)
    logger.debug(f'Send: token')
    token = "{}\n\n".format(ACCOUNT_HASH)
    writer.write(token.encode("utf-8"))
    await writer.drain()
    response = await reader.readline()
    logger.debug(response)
    check_token = response.decode('utf8').replace("'", '"')
    response = await reader.readline()
    logger.debug(response)
    while True:
        if json.loads(check_token) is None:
            logger.debug('Неизвестный токен. Проверьте его или зарегистрируйте заново.')
            break
        message = "{}\n\n".format(message)
        logger.debug(f'Send: {message}')
        writer.write(message.encode('utf-8'))
        await writer.drain()
    logger .debug('Close the connection')
    writer.close()


if __name__ == '__main__':
    message = input()
    asyncio.run(tcp_echo_client(CHAT_HOST, SENDER_PORT, message))