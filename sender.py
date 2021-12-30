import asyncio
from config import CHAT_HOST, SENDER_PORT, ACCOUNT_HASH
import logging
import json


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('SENDER')

async def submit_message(chat_host, chat_port, message):
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


async def register(chat_host, chat_port, nickname):
    logger.debug("Registration")
    reader, writer = await asyncio.open_connection(
            chat_host, chat_port)
    response = await reader.readline()
    logger.debug(response)
    writer.write("\n".encode("utf-8"))
    await writer.drain()
    response = await reader.readline()
    logger.debug(response)
    response_decode = response.decode('utf8').replace("'", '"')
    nickname = "{}\n\n".format(nickname)
    logger.debug(f'Send nickname: {nickname}')
    writer.write(nickname.encode("utf-8"))
    await writer.drain()
    response = await reader.readline()
    logger.debug(response)
    response_decode = response.decode('utf8').replace("'", '"')
    user_info = json.loads(response_decode)
    logger .debug('Close the connection')
    writer.close()
    return user_info['nickname'], user_info['account_hash']


async def authorise(chat_host, chat_port, nickname, message):
    nick, hash = await register(chat_host, chat_port, nickname)
    logger.debug("Authorization")
    reader, writer = await asyncio.open_connection(
            chat_host, chat_port)
    await submit_message(chat_host, chat_port, message)


if __name__ == '__main__':
    message = input()
    asyncio.run(register(CHAT_HOST, SENDER_PORT,message))
    #asyncio.run(submit_message(CHAT_HOST, SENDER_PORT, message))