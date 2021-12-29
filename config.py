import os
from dotenv import load_dotenv

load_dotenv()

CHAT_HOST = os.getenv('CHAT_HOST', 'host')
CHAT_PORT = os.getenv('CHAT_PORT', 'port')
HISTORY_PATH = os.getenv('HISTORY_PATH', 'test.txt')