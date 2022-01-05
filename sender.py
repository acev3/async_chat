import asyncio
from config import CHAT_HOST, SENDER_PORT, ACCOUNT_HASH, USERNAME
import logging
import json
import aiofiles
import argparse


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('SENDER')


def sanitize(message):
    return '{}'.format(str(message).replace('\n', ' '))


async def submit_message(chat_host, chat_port, message, ACCOUNT_HASH):
    reader, writer = await authorise(chat_host, chat_port, ACCOUNT_HASH)
    response = await reader.readline()
    logger.debug(response)
    response = await reader.readline()
    logger.debug(response)
    try:
        while True:
            message = sanitize(message)
            logger.debug(f'San message {message}')
            message = '{}\n\n'.format(message)
            logger.debug(f'Send: {message}')
            writer.write(message.encode('utf-8'))
            await writer.drain()
    except asyncio.CancelledError:
        logger.debug('Client was disconnected')
        raise
    finally:
        logger .debug('Close the connection')
        writer.close()


async def register(chat_host, chat_port, nickname, path_to_keys='keys.json'):
    logger.debug('Registration')
    reader, writer = await asyncio.open_connection(
            chat_host, chat_port)
    response = await reader.readline()
    logger.debug(response)
    writer.write('\n'.encode('utf-8'))
    await writer.drain()
    response = await reader.readline()
    logger.debug(response)
    response_decode = response.decode('utf8').replace("'", '"')
    nickname = '{}\n\n'.format(nickname)
    logger.debug(f'Send nickname: {nickname}')
    writer.write(nickname.encode("utf-8"))
    await writer.drain()
    response = await reader.readline()
    logger.debug(response)
    response_decode = response.decode('utf8').replace("'", '"')
    user_info = json.loads(response_decode)
    logger .debug('Close the connection')
    writer.close()
    async with aiofiles.open(path_to_keys, mode='a') as f:
        await f.write('{}:{}\n'.format(user_info['nickname'], user_info['account_hash']))
    return user_info['nickname'], user_info['account_hash']


async def authorise(chat_host, chat_port, ACCOUNT_HASH):
    logger.debug('Authorization')
    reader, writer = await asyncio.open_connection(
            chat_host, chat_port)
    response = await reader.readline()
    logger.debug(response)
    logger.debug(f'Send: token')
    token = '{}\n\n'.format(ACCOUNT_HASH)
    writer.write(token.encode('utf-8'))
    await writer.drain()
    response = await reader.readline()
    logger.debug(response)
    check_token = response.decode('utf8').replace("'", '"')
    if json.loads(check_token) is None:
        logger.debug('Неизвестный токен. Проверьте его или зарегистрируйте заново.')
        logger .debug('Close the connection')
        writer.close()
    return reader, writer


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, help='Set host')
    parser.add_argument('--port', type=int, help='Set port')
    parser.add_argument('--token', type=str, help='Set token')
    parser.add_argument('--username', type=str, help='Set username')
    parser.add_argument('--message', type=str, help='Set message', required=True)
    args = parser.parse_args()
    chat_host =  args.host or CHAT_HOST
    chat_port = args.port or SENDER_PORT
    token = args.token or ACCOUNT_HASH
    username = args.username or USERNAME
    message = args.message
    asyncio.run(submit_message(CHAT_HOST, SENDER_PORT, message, token))