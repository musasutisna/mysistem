import os
import asyncio
import datetime
import docker
from telegram import Bot
from telegram.error import TelegramError

# Your Telegram bot token and chat ID
TELEGRAM_TOKEN = os.environ['CHECK_CONTAINER_TELEGRAM']
TELEGRAM_CHAT_ID = os.environ['CHECK_CONTAINER_CHATID'].split(';')

# Initialize Docker client
client = docker.from_env()

# List container to watch
CONTAINERS = os.environ['CHECK_CONTAINER_LIST'].split(';')

# Initialize Telegram bot
bot = Bot(token=TELEGRAM_TOKEN)

async def check_container_status(container_name):
  try:
    container = client.containers.get(container_name)

    if container.status != 'running':
      await send_telegram_message(f"Alert: The container '{container_name}' is down!", 0)
  except docker.errors.NotFound:
    await send_telegram_message(f"Alert: The container '{container_name}' is not found!", 0)

async def send_telegram_message(message, index):
  if index < len(TELEGRAM_CHAT_ID):
    try:
      await bot.send_message(chat_id=TELEGRAM_CHAT_ID[index], text=message)
    
      print_with_date(f"Message sent: {message}")

      await send_telegram_message(message, index + 1)
    except TelegramError as e:
      print_with_date(f"Failed to send message: {e}")

def print_with_date(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{current_time}] {message}")

async def checkMultipleContainer(index):
  if index < len(CONTAINERS):
    await check_container_status(CONTAINERS[index])
    await checkMultipleContainer(index + 1)

if __name__ == "__main__":
  loop = asyncio.get_event_loop()

  try:
    loop.run_until_complete(checkMultipleContainer(0))
  finally:
    loop.close()
