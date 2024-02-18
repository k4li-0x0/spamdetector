from pyrogram import Client, types
from pathlib import Path
from alive_progress import alive_bar
import pandas as pd
from asyncio import run
from os import getenv
from dotenv import load_dotenv


load_dotenv('.env')


safeint = lambda x, default=-1, base=10: (
    int(x, base=base) if isinstance(x, str) and x.isnumeric() else default
)


api_id = int(getenv('TELEGRAM_API_ID'))
api_hash = getenv('TELEGRAM_API_HASH')
MAX_MESSAGES_PER_CHANNEL = safeint(getenv('MAX_MESSAGES_PER_GROUP'), default=1000)

CHATS_LIST = [
    '@prographon',
    'https://t.me/+gkH1aZPCnBRiYzUy',
    '@piarchat7890',
    '@genshix_chat',
    '@Deepchat7',
    '@steamzadrot',
    '@weyz1chat',
    '@chatchickengun1',
]


async def main():
    messages = []
    try:
        async with Client('anon', api_id, api_hash) as app:
            app: Client
            for chat_link in CHATS_LIST:
                chat = await app.get_chat(chat_link)  # structure with chat id
                if chat is types.ChatPreview:
                    print(
                        f'<TG Messages Parser> {chat_link} skipped, because it\'s private and you are not subscribed to it'
                    )
                    continue
                print(f'<TG Messages Parser> Reading: {chat.first_name or chat.title}')
                total = min(
                    await app.get_chat_history_count(chat.id), MAX_MESSAGES_PER_CHANNEL
                )  # just for progress bar
                with alive_bar(total, title=(chat.first_name or chat.title)) as bar:
                    async for message in app.get_chat_history(
                        chat.id, MAX_MESSAGES_PER_CHANNEL
                    ):
                        if (
                            message.text is not None
                        ):  # text can be None, if message is just a picture, for example
                            messages.append(
                                (
                                    chat.id,
                                    message.id,
                                    message.reply_to_message_id or -1,
                                    message.text,
                                )
                            )
                        bar()
    except Exception as e:
        print('<TG Messages Parser>', e)
        print('<TG Messages Parser> Saving existing messages')
    dataset_path = Path() / 'dataset'
    dataset_path.mkdir(exist_ok=True)
    dataset_path /= 'messages.csv'
    df = pd.DataFrame(
        messages, columns=['chat_id', 'message_id', 'reply_id', 'message']
    )
    df.to_csv(dataset_path)


run(main())
