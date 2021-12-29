import os
from dotenv import load_dotenv

load_dotenv()

CHAT_HOST = os.getenv('CHAT_HOST', 'host')
CHAT_PORT = os.getenv('CHAT_PORT', 'port')
HISTORY_PATH = os.getenv('HISTORY_PATH', 'test.txt')
SENDER_PORT = os.getenv('SENDER_PORT','5050')
ACCOUNT_HASH = os.getenv('ACCOUNT_HASH','123')