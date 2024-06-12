import os
from telethon import TelegramClient
from config import telegram_params
from component_samples.base_handler import (new_message_handler,
                                            user_update_handler)

# Init session folder
os.makedirs(telegram_params.session_dir, exist_ok=True)
# Define session path
session_name = "voice_bot"
session_path = os.path.join(telegram_params.session_dir, session_name)

def main():
    # Validating infor
    assert telegram_params.api_id, "API ID cant be None"
    assert telegram_params.api_hash, "API HASH cant be None"
    assert telegram_params.bot_token, "BOT Token cant be None"

    # Login
    client = TelegramClient(
        session = session_path,
        api_id = telegram_params.api_id,
        api_hash = telegram_params.api_hash)

    # Start client
    client.start(bot_token = telegram_params.bot_token)

    # Define event handler
    event_handlers = [new_message_handler,user_update_handler]
    # Add event
    for handler in event_handlers: client.add_event_handler(handler)

    # client.send_file()
    # Run the server
    print("Bot Service is on!")
    # client.loop.run_until_complete(main())
    client.run_until_disconnected()

if __name__ == "__main__":
    main()