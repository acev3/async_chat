import asyncio
from config import CHAT_HOST, SENDER_PORT, ACCOUNT_HASH

async def tcp_echo_client(chat_host, chat_port, message):
    reader, writer = await asyncio.open_connection(
            chat_host, chat_port)
    while True:
        response = await reader.readline()
        print(response)
        print(f'Send: HASH')
        token = "{}\n".format(ACCOUNT_HASH)
        writer.write(token.encode("utf-8"))
        await writer.drain()
        response = await reader.readline()
        print(response)
        reader, writer = await asyncio.open_connection(
            chat_host, chat_port)
        message = "{}\n".format(message)
        print(f'Send: {message}')
        writer.write(message.encode('utf-8'))
        await writer.drain()
        print(f'Send: {message}')
        writer.write(message.encode('utf-8'))
        await writer.drain()
    print('Close the connection')
    writer.close()


if __name__ == '__main__':
    message = input()
    asyncio.run(tcp_echo_client(CHAT_HOST, SENDER_PORT, message))